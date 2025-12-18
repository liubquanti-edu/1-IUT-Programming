import random

notes = []

for i in range(10):
    notes.append(f'Nom {i + 1}')
    for j in range(4):
        note = random.randint(0, 20)
        notes.append(note)
    total = sum(notes[-4:])
    moy = total / 4
    notes.append(moy)
    print(notes)
    notes = []