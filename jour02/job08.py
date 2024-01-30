import mysql.connector

class ZooManager:
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='zoo'
        )
        self.curseur = self.connexion.cursor()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        sql = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        valeurs = (nom, race, id_cage, date_naissance, pays_origine)
        self.curseur.execute(sql, valeurs)
        self.connexion.commit()

    def supprimer_animal(self, id_animal):
        sql = "DELETE FROM animal WHERE id = %s"
        valeurs = (id_animal,)
        self.curseur.execute(sql, valeurs)
        self.connexion.commit()

    def afficher_animaux(self):
        sql = "SELECT * FROM animal"
        self.curseur.execute(sql)
        resultats = self.curseur.fetchall()
        for resultat in resultats:
            print(resultat)

    def afficher_animaux_cages(self):
        sql = "SELECT cage.id, cage.superficie, cage.capacite_max, animal.* FROM cage LEFT JOIN animal ON cage.id = animal.id_cage"
        self.curseur.execute(sql)
        resultats = self.curseur.fetchall()
        for resultat in resultats:
            print(resultat)

    def calculer_superficie_totale(self):
        sql = "SELECT SUM(superficie) AS superficie_totale FROM cage"
        self.curseur.execute(sql)
        resultat = self.curseur.fetchone()
        superficie_totale = resultat[0]
        print(f"La superficie totale de toutes les cages est de {superficie_totale} m2")

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()

# Exemple d'utilisation
if __name__ == "__main__":
    zoo_manager = ZooManager()

    zoo_manager.ajouter_animal('Lion', 'Félin', 1, '2020-01-15', 'Afrique')

    zoo_manager.afficher_animaux()

    zoo_manager.afficher_animaux_cages()

    zoo_manager.calculer_superficie_totale()
    
    zoo_manager.fermer_connexion()
