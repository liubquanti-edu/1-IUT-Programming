lim = int(input("Quel total maximum ? "))

i = 0
total = 0
while total + 1 <= lim:
    total = total + i
    i = i + 1

i = i - 1

print(f"La somme de 1 à {i} fait {total} et est ≥ à {lim}")