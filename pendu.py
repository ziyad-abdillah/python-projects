import random

def pendu():
    niveau = input("taper 1(debutant) 2(intermediaire) ou 3(expert) pour le niveau")
    
    if niveau == "1" or niveau == "2" or niveau == "3":
        with open("dico_france.txt","r",encoding="ISO-8859-1") as file:
            lecture = file.read()
            liste = lecture.split()
            mot = (random.choice(liste))
            

        afficher = []

        for i in mot:
            afficher.append('_')

        print(" ".join(afficher))

        if niveau == "1":
            vie = 10
        elif niveau == "2":
            vie = 7
        else:
            vie = 3        
        
        lettres_trouvees = ''

        while vie > 0:
            print("Vous avez", vie, "vie(s)")
            lettre = input("Entrez une lettre : ")    
            lettres_trouvees = lettres_trouvees + lettre
            if niveau != "3":
                print("Lettre utilisé :"," ".join(lettres_trouvees))

            if lettre in mot:
                count = 0
                for j in mot:
                    if lettre == j:
                        afficher[count] = lettre
                    count = count + 1                    
            else:
                vie = vie - 1
            print(" ".join(afficher))
            if '_' not in afficher:
                print("Gagné")
                quit()

        if '_' in afficher:
            print('Perdu')
            print('Le mot était :', mot)
            quit()

pendu()