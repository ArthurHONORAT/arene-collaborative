# Moteur de combat occitanie
def initialiser_arene(nom :str):
    return {"nom": nom, "combattants": []}

def attaque_charge():
    return "Charge inflige 20 dégâts bruts"

def boire_potion(points: int = 30):
    return f"Soin de {points} PV"


print("Moteur de jeu chargé.")
print("Système prêt.")

def determiner_initiative(vitesse_a: int, vitesse_b: int) -> str:
    if vitesse_a >= vitesse_b:
        return "combattant_a"
    return "combattant_b"