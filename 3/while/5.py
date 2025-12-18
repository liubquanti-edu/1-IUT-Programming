e = int(input("Saisir un entier > 0 : "))

i = 1
rf = 1

for i in range(1, e + 1):
    rf = rf * i

print(f"{e}! = {rf} (for)")

i = 1
rw = 1

while i <= e:
    rw = rw * i
    i = i + 1

print(f"{e}! = {rw} (while)")