import mysql.connector


config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',  
    'database': 'LaPlateforme',
}


connexion = mysql.connector.connect(**config)

curseur = connexion.cursor()

curseur.execute("SHOW TABLES")

resultats = curseur.fetchall()
print("Tables dans la base de données LaPlateforme:", resultats)

curseur.close()
connexion.close()
