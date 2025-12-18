import random

number = random.randint(0, 100)

print("Deviner un entier entre 0 et 100.")

i = 0
imin = 0
imax = 100

while i != number:
    i = int(input(f"Votre proposition entre {imin} et {imax} ? "))
    if i < number:
        print(f"{i} est trop petit.")
        imin = i
    elif i > number:
        print(f"{i} est trop grand.")
        imax = i
    else:
        print(f"{i} est bien le nombre a trouver.")