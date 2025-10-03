a=float(input("veuillez saisir la valeur de a : "))

b=float(input("veuillez saisir la valeur de b : "))

o=str(input("veuillez saisir l'opération que vous souhaiter effectuer: "))

if o=="D" and b>0 :

    print("le résultat est : ", "{:.2f}".format(a/b))

elif o=="A" :

    print("le résultat est : ", a+b)

elif o=="S" :

    print("le résultat est : ", a-b)

elif o=="M" :

    print("le résultat est : ", a*b)

else :

    print("veuillez sasir les bonne information")