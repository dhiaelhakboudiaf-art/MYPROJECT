import random

s = random.randint(1 , 30)

for i in range(1 , 6):

    n = int(input("choisir un nombre: "))

    if n < s:

        print("trop petit")

    elif n == s:

        print("vous avez trouvez le bon nombre en",i,"essai")

        break

    else:

        print("trop grand")

if n != s:

    print(" le nombre d'essai est terminer. Le nombre est:",s)
