a = int(input( " Entrez une date : "))

if(a>=1994):
    if(a!=1916 and a!=1940 and a!= 1944):
        if((a%4==0 and a%100!=0 or a%400==0) or (a%4==2 and a%100!=2 or a%400==2)):
            print("True")
        else:
            print("False")
    else:
        print("False")
else:
	print("False")