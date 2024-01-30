import mysql.connector


config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',  
    'database': 'LaPlateforme',
}

connexion = mysql.connector.connect(**config)

curseur = connexion.cursor()


curseur.execute("SELECT SUM(capacite) AS capacite_totale FROM salle")


resultat = curseur.fetchone()

capacite_totale = resultat[0]
print(f"La capacité totale des salles est de : {capacite_totale} ")


curseur.close()
connexion.close()
