import random

total = 0

for i in range(10):
    note = random.randint(0, 20)
    print(f"Note n°{i} : {note}")
    total += note

print(f"Moyenne : {total / 10:.2f}")