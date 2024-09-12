#coding:utf-8
'''
operateur de comparaison:   ==(Egal A)
                            !=(different de)
                            < (plus peti que)
                            >(plus grand que)
                            <=(plus petit ou egal)
                            >=(plus grand ou egal)
                            
Mots Cles des conditions: if /elif/ else                            
conditions multiples    : and (ET)  
                          or(OUI)
                          in/not in (DANS/ PAS DANS)                        
'''


identifiant="jason"
mot_de_pass="password123"

print("interface de connexion")

user_id=input("Entrez votre identifiant:")

user_password=input("Entrez votre mot de pass:")

  

if user_id==user_id or user_password==mot_de_pass:
    print("Bienvenu vous etes connectee",user_id)

   
print("Vous avez oublie l'identifiant ou le mots de pass")
