import random

number = random.randint(0, 100)

print("Deviner un entier entre 0 et 100.")

i = 0

while i != number:
    i = int(input("Votre proposition ? "))
    if i < number:
        print(f"{i} est trop petit.")
    elif i > number:
        print(f"{i} est trop grand.")
    else:
        print(f"{i} est bien le nombre a trouver.")