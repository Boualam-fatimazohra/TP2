import sys  # N'oubliez pas d'importer le module sys
while True:
    prix = float(input("Saisissez un prix : "))
    
    if (prix < 0):
        print("oups! le nombre doit etre superieur a zero.")
        sys.exit()  # Utilisez sys.exit() avec des parenthèses pour quitter le programme

    if (prix > 0):
        choix = input("Voulez-vous convertir en DH ou E : ")
        if choix == 'DH':
            prix = prix * 0.092
        else:
            prix = prix * 10.86
        print("Le prix converti est :", prix)
    else:
        print("Le nombre doit être supérieur à zéro")
