def contenuHTML(contenu):
    print(contenu)
    with open("ex.html", "w") as ficIndex:
        ficIndex.write(contenu)

contenuHTML("""<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Exercice 4</title>
    </head>
    <body>
        <h1>Hello world!</h1>
    </body>
</html>""")