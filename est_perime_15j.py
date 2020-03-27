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
    print("False")
    
elif(datemax.strftime("%Y")==dateact.strftime("%Y")):
    if(datemax.strftime("%m")>=dateact.strftime("%m")):
        if(datemax.strftime("%d")>=dateact.strftime("%d")):
            print("False")
        
        elif(datemax.strftime("%m")>dateact.strftime("%m")):
            print("False")
        
        else:
            print("True")
    else:
        print("True")

else:
    print("True")
    
