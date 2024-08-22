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
'''
agePersonne=10
agePersonne2=12
agePersonne3=12.6
nomPersonne="MUKIZA"
ages=agePersonne*agePersonne2
ages2=ages+agePersonne3

texte=" les personnes ont {} ages le represantant c'est {}."
print(texte.format(ages,nomPersonne))

print(" les personnes ont {} ages le represantant c'est {}.".format(ages,nomPersonne))

# print("Age de la personne numero 1 est",agePersonne) #affichage de l'agePersonne
# print("Age de la personne numero 2 est",agePersonne2)
# print(" Total des ages pour les deux personnes est egal \n \t A ",ages)# c'est pour affiche l'age de personne
# print(ages2)

# print(nomPersonne) #afficher le nom de personne
