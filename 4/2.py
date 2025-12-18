esec = int(input("Quelle durée (en s) ? "))

sec = esec % 60
min = (esec // 60) % 60
heure = (esec // 3600) % 24
jour = esec // 86400

print(
    (f"{esec} secondes representent ") +
    (f"{jour} jour " if jour == 1 else "") +
    (f"{jour} jours " if jour > 1 else "") +
    (f"{heure} heure " if heure == 1 else "") +
    (f"{heure} heures " if heure > 1 else "") +
    (f"{min} minute " if min == 1 else "") +
    (f"{min} minutes " if min > 1 else "") +
    (f"{sec} seconde" if sec == 1 else "") +
    (f"{sec} secondes" if sec > 1 else "") +
    "."
)