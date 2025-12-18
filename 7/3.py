import random

number = random.randint(0, 100)

print("Deviner un entier entre 0 et 100.")

i = 0
imin = 0
imax = 100
idef = imin + (imax - imin) // 2

while i != number:
    a = input(f"Votre proposition entre {imin} et {imax} ({idef} par défault) ? ")
    if a == "":
        i = idef
    else:
        i = int(a)
    if i < number:
        print(f"{i} est trop petit.")
        imin = i
        idef = imin + (imax - imin) // 2
    elif i > number:
        print(f"{i} est trop grand.")
        imax = i
        idef = imin + (imax - imin) // 2
    else:
        print(f"{i} est bien le nombre a trouver.")