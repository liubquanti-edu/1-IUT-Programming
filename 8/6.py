def saisirIp():
    return input("Saisir une adresse IP au format décimal pointé : ")

def decoupIp(adrIp):
    return list(map(int, adrIp.split('.')))

def classeIp(adrIp):
    premier_octet = decoupIp(adrIp)[0]
    if 0 <= premier_octet <= 127:
        return 'A'
    elif 128 <= premier_octet <= 191:
        return 'B'
    elif 192 <= premier_octet <= 223:
        return 'C'
    elif 224 <= premier_octet <= 239:
        return 'D'
    elif 240 <= premier_octet <= 255:
        return 'E'

def masqueStandard(adrIp):
    classe = classeIp(adrIp)
    if classe == 'A':
        return "255.0.0.0"
    elif classe == 'B':
        return "255.255.0.0"
    elif classe == 'C':
        return "255.255.255.0"
    elif classe == 'D':
        return "255.255.255.255"
    elif classe == 'E':
        return "Pas de masque"

def reseauIp(adrIp):
    octets = decoupIp(adrIp)
    classe = classeIp(adrIp)
    if classe == 'A':
        return f"{octets[0]}.0.0.0"
    elif classe == 'B':
        return f"{octets[0]}.{octets[1]}.0.0"
    elif classe == 'C':
        return f"{octets[0]}.{octets[1]}.{octets[2]}.0"
    elif classe == 'D':
        return "Adresse multicast"
    elif classe == 'E':
        return "Adresse réservée"

if __name__ == "__main__":
    adrIp = saisirIp()
    print(f"Classe : {classeIp(adrIp)}")
    print(f"Masque standard : {masqueStandard(adrIp)}")
    print(f"Réseau IP : {reseauIp(adrIp)}")