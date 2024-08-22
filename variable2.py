#coding:utf-8
'''''
Nommer une variable: doit commancer par une lettre
ou underscore
ne pas contenir des caracteres speciaux
ne pas contenir d'espaces
utiliser des underscores (_)
le python n'accepte pas les caracteres speciaux

Types standards    : entier numerique (int)
                     nombre flottant (float)
                     chaine de caracteres (str)
                     booleen (bool)
                     autres (listes, dictionnaires, tuples etc, )
                     
Fonction Vues:      print()     --> afficher A l'ecran
                    input()     --> Lire au clavier
                    type()      --> retourne le type d'une donnee, variable, etc.
                    int(), float(), str(), bool() -> "caster" une donnee, la convertir
                    str.format()--> formater une chaine de caractere                      
'''
#premiere example
salt="Mr, Mme:"
print("Bonjour :", salt)#affichage de message "Bienvenue" et le nom de joueur

###########Autres example######
nom= input("Choisissez un nom de joueur")

print("Bienvenue,", nom)
######## Autres ex
prixHT=input("Entrez un prix HT:  ")
prixHT=int(prixHT)
prixTTC=prixHT+(prixHT * 20/100)

print("Prix TTC =", prixTTC)