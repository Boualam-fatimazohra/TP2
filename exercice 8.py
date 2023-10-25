# Demander à l'utilisateur de saisir le nombre à rechercher
nombre_recherche = int(input("Entrez le nombre que vous voulez rechercher : "))

# Créer une liste d'exemple 
liste = [5, 7, 2, 5, 8, 5, 9, 3, 5]

# Initialiser un compteur pour les occurrences
occurrences = 0

# Parcourir la liste pour compter les occurrences du nombre recherché
for nombre in liste:
    if nombre == nombre_recherche:
        occurrences += 1

# Afficher le résultat
print(f"Le nombre {nombre_recherche} apparaît {occurrences} fois dans la liste.")
