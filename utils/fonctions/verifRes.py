import datetime
def verifRes(list):
    nom = list[0].split(" ")
    for elem in nom:
        for lettre in elem:
            if not isinstance(str(lettre),str) or not str(lettre).isalpha():
                print("Mauvais format nom client")
                break
    for chiffre in list[1].split(" "):
        print(chiffre)
        if not str(chiffre).isnumeric():
            print("Pas bon format de numéro de téléphone")
    try:
        if not datetime.datetime.strptime(list[2] ,'%Y-%m-%d %H:%M'):
            print("mauvais format de date")
    except TypeError:
        print("Mauvais format de date")
    except ValueError:
        print("Mauvais format date")      
    
    if not str(list[3]) in ["eu","azy","an","as","af"]:
        print("Print mauvais type de cuisine veuillez rentrer")
        
    if not str(list[4]).lower() in ["oui","non"]:
        print("Il y'a t'il des pmr ? Oui-Non")
    #elif str(list[4]).lower() == "oui":
        #return True
    #else:
        #return False
    
    if not str(list[5]).lower() in ["oui","non"]:
        print("Il y'a t'il des bébé ? Oui-Non")

    #if not int(list[6]) and int(list[6]) not in listTableId:
        #print("Numéro de table pas valide !")



#verifRes(["456","0afea","202-12-02 21:2","eu","oui","oui"])