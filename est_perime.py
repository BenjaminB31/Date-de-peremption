datejour = int(input( " Jour actuel : "))
datemois = int(input( " Mois actuel : "))
dateannee = int(input( " Annee actuelle : "))

datedlcjour = int(input( " Jour de la DLC : "))
datedlcmois = int(input( " Mois de la DLC : "))
datedlcannee = int(input( " Annee de la DLC : "))

if(datedlcannee>dateannee):
    print("False")
    
elif(datedlcannee==dateannee):
    if(datedlcmois>=datemois):
        if(datedlcjour>=datejour):
            print("False")
            
        else:
            print("True")
    else:
        print("True")

else:
    print("True")
    