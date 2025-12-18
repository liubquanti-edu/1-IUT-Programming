bInf = int(input("Quelle borne inf > 0 ? "))
bSup = int(input(f"Quelle borne sup > {bInf} ? "))

r = 0
for cpt in range(bInf, bSup + 1):
    r = r + cpt

print(f"Total : {r}")
