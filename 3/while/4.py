e = int(input("Saisir un entier > 1 : "))

d = e - 1
while d > 1 and e % d != 0:
    d = d - 1

print(f"Le plus grand diviseur de {e} est {d}")