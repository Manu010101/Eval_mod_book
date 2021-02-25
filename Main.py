
from scrap.Oddsportal import Oddsportal

##
# partie acquisition

# RECUPERATION ET SAUVEGARDE D UNE SAISON D UN CHAMPIONNAT - à titre d'exemple seulement, code construit pour récupérer
# toutes les données d'un championnat mais plus long....

o = Oddsportal("https://www.oddsportal.com/basketball/usa/nba-2014-2015/results/")
donnees = o.recupere_donnees_saison(url_base_saison="https://www.oddsportal.com/basketball/usa/nba-2014-2015/results/")
o.sauvegarde_donnees_saison(nom_table="nba_2014_2015", donnees_a_sauvegarder=donnees)

# RECUPERATION ET SAUVEGARDE DE TOUTES LES SAISONS D UN CHAMPIONNAT (long, heure)
# o = Oddsportal("https://www.oddsportal.com/soccer/france/ligue-1/results/")
# o.recupere_et_sauvegarde_saisons()
