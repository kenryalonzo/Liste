import sys

LISTE = []

MENU = """Choisissez parmis les 5 options suivantes :
1- Ajouter un element à la liste 
2- Retirer un element de la liste
3- Afficher la liste
4- Vider la liste
5- Quitter
Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICES:
        print("Veuillez choisir une option valide...")
        continue

    if user_choice == "1": #Ajout des element
       item = input("Entrez le nom d'un element a ajouter a la liste de courses : ")
       LISTE.append(item)
       print(f"L'element {item} a bien ete ajoute a la liste.")

    elif user_choice == "2": #Retirer un element
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")

    elif user_choice == "3":  # Afficher la liste
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun element.")

    elif user_choice == "4":  # Vider la liste
        LISTE.clear()
        print("La liste a été vidée de son contenu.")

    elif user_choice == "5":  # Quitter
        print("À bientôt !")
        print( "\t\t---------------------------------------------DEVELOPED BY GHOST---------------------------------------------\n\n")
        sys.exit()
        print("-" * 50)
