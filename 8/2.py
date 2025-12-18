def est_palindrome(mot):
    mot = mot.lower()
    return mot == mot[::-1]

mot = input("Saisir une phrase : ")

if est_palindrome(mot):
    print(f"{mot} est un palindrome.")
else:
    print(f"{mot} n'est pas un palindrome. Preuve : {mot[::-1].lower()}")