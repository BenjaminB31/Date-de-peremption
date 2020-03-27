import datetime
from datetime import timedelta

datejour = int(input( " Jour actuel : "))
datemois = int(input( " Mois actuel : "))
dateannee = int(input( " Annee actuelle : "))

datedlcjour = int(input( " Jour de la DLC : "))
datedlcmois = int(input( " Mois de la DLC : "))
datedlcannee = int(input( " Annee de la DLC : "))

dateact = datetime.datetime(dateannee, datemois, datejour)
datedlc = datetime.datetime(datedlcannee, datedlcmois, datedlcjour)
adddate = datetime.timedelta(days=15)
datemax = datedlc + adddate

if(datemax.strftime("%Y")>dateact.strftime("%Y")):
    print("False1")
    
elif(datemax.strftime("%Y")==dateact.strftime("%Y")):
    if(datemax.strftime("%m")>=dateact.strftime("%m")):
        if(datemax.strftime("%d")>=dateact.strftime("%d")):
            print("False2")
        
        elif(datemax.strftime("%m")>dateact.strftime("%m")):
            print("False3")
        
        else:
            print("True1")
    else:
        print("True2")

else:
    print("True3")
    