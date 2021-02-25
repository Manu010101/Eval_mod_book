import sqlite3

from bd.glob import Glob


class BD:
    
    def __init__(self, base_donnees):
        """
        Instancie une connexion à la base de données et un curseur
        :param base_donnees: nom de la base de donnée
        """
        self.bd = None
        try:
            self.bd = sqlite3.connect(base_donnees)
            self.curseur = self.bd.cursor()
        except Exception as e:
            print(e)
            
    def commit(self):
        if self.bd:
            self.bd.commit()
            
    def close(self):
        if self.bd:
            self.curseur.close()
            self.bd.close()
    
    def creer_table(self, nom_table, descripteur ='donnees_paris'):
        """
        Création d'une table nommée nom_table pour stocker les données entrée d'un pari.
        :param nom_table: de préférence de format pari_date
        :return:
        """

        req = f"CREATE TABLE IF NOT EXISTS {nom_table} ("  # requête SQL construite par concaténation en parcourant
        # le modèle de table stocké dans Glob.DIC_TABLE
        
        descripteurs = Glob.DIC_TABLE[descripteur]  # description de chaque champ de la table donnees_paris
        for i, description in enumerate(descripteurs):  # parcours les descriptions des champs
            nom_champ = description[0]
            indication_type_champ = description[1]
            type_champ = ""
            if "t" in indication_type_champ:
                type_champ = "TEXT"
            if "r" in indication_type_champ:
                type_champ = "REAL"
            if "i" in indication_type_champ:
                type_champ = "INTEGER"
            if "k" in indication_type_champ:
                type_champ = type_champ + " PRIMARY KEY"
            if "n" in indication_type_champ:
                type_champ = type_champ + " NULL"
            # fin de la concaténation de la requête, si dernier bout on finit par ), sinon ,
            if i != len(descripteurs) - 1:
                req = req + f"{nom_champ} {type_champ},"
            else:
                req = req + f"{nom_champ} {type_champ})"
        print(Glob.couleur_verte)
        print(req)
        print(Glob.par_defaut)
        try:
            self.curseur.execute(req)
            self.commit()
        except Exception as e:
            print(e)
    
    def insere_matchs(self, *, nom_table, my_donnees):
        
        nb_valeurs_a_inserer = len(my_donnees[0])
        bout_requete = "(" + (nb_valeurs_a_inserer - 1) * "?," + "?)"
        requete_inertion = f" INSERT INTO {nom_table} VALUES " + bout_requete
        try:
            self.curseur.executemany(requete_inertion, my_donnees)
            self.commit()
        except Exception as e:
            print(e)
            
    def execute_requete(self, *, requete_SQL):
        
        self.curseur.execute(requete_SQL)
        resultat = self.curseur.fetchone()
        # self.close()
        return resultat[0]  # fetch rend un tuple qu'on transforme en str pour pouvoir utiliser dans le reste du prog
