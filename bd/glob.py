class Glob:
    """
    Classe contenant les constantes
    """
    
    NOM_BD_SIMU = "bd_simu_oddsportal.db"
    
    # Pour constructiopn auto de table
    DIC_TABLE = {
        "donnees_simu": [
            ("affiche", "t", "affiche du match"),
            ("cote1", "r", "valeur de la première cote"),
            ("cote2", "r", "valeur de la deuxième cote"),
            ("cote3", "r - n", "valeur de la troisième cote"),
            ("gagnant", "t", "gagnant du match"),
            ("favori gagne", "i", "1 si favori gagne 0 sinon")
        ]
    }
    
    
    # partie mise en forme des couleurs
    
    par_defaut = '\033[0m'  # couleur et fond par défaut
    couleur_bleue = '\033[34m'
    couleur_verte = '\033[32m'
    couleur_rouge = '\033[31m'

