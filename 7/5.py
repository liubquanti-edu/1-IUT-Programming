def afficheTableHTML(contenu):
    with open("ex.html", "w") as ficIndex:
        ficIndex.write(contenu)

head = "<tr><th>*</th>" + "".join(f"<th>{i}</th>" for i in range(0, 9)) + "</tr>"
body = "".join(
    f"<tr><th>{i}</th>" + "".join(f"<td>{i * j}</td>" for j in range(0, 9)) + "</tr>"
    for i in range(0, 9)
)

table = head + body

contenu = """<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Exercice 5</title>
    </head>
    <body>
        <table border="1px">
            """ + table + """
        </table>
    </body>
</html>"""

afficheTableHTML(contenu)