import mysql.connector


config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',  
    'database': 'LaPlateforme',
}


connexion = mysql.connector.connect(**config)


curseur = connexion.cursor()


curseur.execute("SELECT SUM(superficie) AS superficie_totale FROM etage")

resultat = curseur.fetchone()

superficie_totale = resultat[0]
print(f"La superficie de La Plateforme est de {superficie_totale} m2")


curseur.close()
connexion.close()
