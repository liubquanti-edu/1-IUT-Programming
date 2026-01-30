class Router:
    def __init__ (self, marque, modele, wifi_active):
        self.marque = marque
        self.modele = modele
        self.wifi_active = wifi_active

router1 = Router("TP-Link", "Archer C7", True)
router2 = Router("Netgear", "Nighthawk R7000", False)

print("Marque :", router1.marque)

def activer_wifi(self):
    if not self.wifi_active:
        self.wifi_active = True
        print("WiFi activé")
    else:
        print("Le WiFi est déjà activé")

activer_wifi(router2)