bInf = int(input("Quelle borne inf > 0 ? "))
bSup = int(input("Quelle borne sup > borne inf ? "))
inter = int(input("Quel intervalle > 0 ? "))
p = int(input("Quelle puissance > 0 ? "))

for cpt in range(bInf, bSup + 1, inter):
    print(f"{cpt}^{p} =", cpt ** p)