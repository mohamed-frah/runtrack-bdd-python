import mysql.connector

class Salarie:
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='job07'
        )
        self.curseur = self.connexion.cursor()

    def inserer_salarie(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.curseur.execute(sql, valeurs)
        self.connexion.commit()

    def recuperer_salarie(self, salaire_min):
        sql = "SELECT * FROM employe WHERE salaire > %s"
        valeurs = (salaire_min,)
        self.curseur.execute(sql, valeurs)
        resultats = self.curseur.fetchall()
        return resultats

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()


if __name__ == "__main__":
    salarie = Salarie()
    
    
    salarie.inserer_salarie('Doe', 'John', 3800.00, 1)
 
    resultats = salarie.recuperer_salarie(3000)
    for resultat in resultats:
        print(resultat)

    
    salarie.fermer_connexion()
