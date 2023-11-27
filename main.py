import sqlite3 # pour la base de donnée
import sys # pour quitter le programme
import datetime # pour la date et l'heure
import os # pour effacer le terminal
import time # pour le temps

'''
"""
Programme Python qui permet à l’utilisateur de tenir un bloc-notes personnel. 
L’utilisateur peut ajouter des notes, les lire, les rechercher et les supprimer.
"""

# créez la base de donnée

'''
conn = sqlite3.connect('premiercourspython2023.db') # créez la base de donnée
cursor = conn.cursor() # créez un curseur pour la base de donnée
'''

# créez la table
'''
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        titre VARCHAR(50),
        type VARCHAR(50),
        note TEXT,
        date TEXT
    )
    """)
conn.commit()

class Blocnote:
    """
    Cette classe permet de créer un blocnote
    """
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter(self, note):
        """
        note : Note
        Cette fonction permet d'ajouter une note dans la base de donnée
        """
        try:
            self.notes.append(note)
            cursor.execute("""INSERT INTO notes(titre, type, note, date) VALUES(?, ?, ?, ?)""", (note.titre, note.type, note.note, note.date)) # ajoute la note dans la base de donnée
            conn.commit() # sauvegarde les modifications
        except Exception as error:
            print("Erreur : ", error)

    def rechercher(self, mot):
        """
        mot : str
        Cette fonction permet de rechercher une note dans la base de donnée
        """
        try:
            cursor.execute("""SELECT * FROM notes WHERE titre LIKE ? OR note LIKE ?""", ("%"+mot+"%", "%"+mot+"%"))
            notes = cursor.fetchall()
            print("Voici la liste des notes : ")
            print("/-----------------------------------------/")
            for note in notes:
                print(note)
            print("/-----------------------------------------/")
        except Exception as error:
            print("Erreur : ", error)

    def suppimer(self, titre):
        """
        titre : str
        Cette fonction permet de supprimer une note dans la base de donnée
        """
        try:
            cursor.execute("""DELETE FROM notes WHERE titre = ?""", (titre,))
            conn.commit()
        except Exception as error:
            print("Erreur : ", error)

    def vider_blocnote(self):
        """
        Cette fonction permet de vider le blocnote
        """
        try:
            cursor.execute("""DELETE FROM notes""")
            conn.commit()
        except Exception as error:
            print("Erreur : ", error)

    def afficher(self, type):
        """
        type : str
        Cette fonction permet d'afficher les notes dans la base de donnée
        """
        try:
            cursor.execute("""SELECT * FROM notes WHERE type = ?""", (type,)) # récupère toutes les notes
            notes = cursor.fetchall() # récupère toutes les notes
            print("Voici la liste des notes : ") # affiche un message
            print("/-----------------------------------------/") # affiche un message
            for note in notes: # parcour toutes les notes
                print(note) # affiche les (1par1) note
            print("/-----------------------------------------/") # affiche un message

        except Exception as error:
            print("Erreur : ", error)

class Note:
    def __init__(self, titre, date):
        """
        titre : str
        date : datetime.datetime.now()
        """
        self.titre = titre
        self.date = date
    

class NoteTexte(Note):
    def __init__(self, titre, note, date, type=None):
        """
        titre : str
        note : str
        date : datetime.datetime.now()
        """
        super().__init__(titre, date)
        self.note = note
        self.type = "notesTexte"

class NoteFichier(Note):
    def __init__(self, titre, fichier, date, type=None):
        """
        titre : str
        fichier : str
        date : datetime.datetime.now()
        """
        super().__init__(titre, date)
        self.note = fichier
        self.type = "notesFichier"

blocnoteTest = Blocnote("blocnoteTest")

if __name__ == '__main__':

    while True:

        print("Que voulez-vous faire ?")
        print("1. Ajouter une note")
        print("2. Afficher les notes")
        print("3. Rechercher une note")
        print("4. Supprimer une note")
        print("5. Vider le blocnote")
        print("6. Quitter")
        choix = input("Votre choix : ")

        match choix:

            case "1":
                os.system("clear")
                print("Quel type de note voulez-vous ajouter ?")
                print("1. Note texte")
                print("2. Note fichier")

                match input("Votre choix : "):

                    case "1":
                        os.system("clear")
                        titre = input("Titre de la note : ")
                        note = input("Note : ")
                        date = datetime.datetime.now()
                        noteTexte = NoteTexte(titre, note, date)
                        blocnoteTest.ajouter(noteTexte)
    
                    case "2":
                        os.system("clear")
                        titre = input("Titre de la note : ")
                        fichier = input("Fichier : ")
                        date = datetime.datetime.now()
                        noteFichier = NoteFichier(titre, fichier, date)
                        blocnoteTest.ajouter(noteFichier)

                    case _:
                        print("Erreur : Veuillez choisir entre 1 et 2")
    
            case "2":
                os.system("clear")
                print("Quel type de note voulez-vous afficher ?")
                print("1. Note texte")
                print("2. Note fichier")
    
                match input("Votre choix : "):
                        
                    case "1":
                        os.system("clear")
                        blocnoteTest.afficher("notesTexte")
    
                    case "2":
                        os.system("clear")
                        blocnoteTest.afficher("notesFichier")

                    case _:
                        print("Erreur : Veuillez choisir entre 1 et 2")
    
            case "3":
                os.system("clear")
                mot = input("Mot à rechercher : ")
                blocnoteTest.rechercher(mot)
    
            case "4":
                os.system("clear")
                title = input("Titre de la note à supprimer : ")
                blocnoteTest.suppimer(title)
    
            case "5":
                os.system("clear")
                blocnoteTest.vider_blocnote()
    
            case "6":
                os.system("clear")
                print("Au revoir !")
                time.sleep(1)
                sys.exit()
    
