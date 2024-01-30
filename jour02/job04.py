import mysql.connector


config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost', 
    'database': 'LaPlateforme',
}


connexion = mysql.connector.connect(**config)

curseur = connexion.cursor()

curseur.execute("SELECT nom, capacite FROM salle")

resultats = curseur.fetchall()

for resultat in resultats:
    nom, capacite = resultat
    print(f"( {nom}, {capacite})")


curseur.close()
connexion.close()
