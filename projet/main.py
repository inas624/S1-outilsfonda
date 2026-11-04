"""Comparaison de pizzas par surface et par prix. Python standard uniquement."""
import math
from pathlib import Path

PIZZAS = [
    {"nom": "Petite", "diametre": 26.0, "prix": 9.00},
    {"nom": "Moyenne", "diametre": 30.0, "prix": 11.00},
    {"nom": "Grande", "diametre": 34.0, "prix": 13.00},
]

def surface_pizza(diametre):
    """Calcule la surface d'une pizza circulaire en cm²."""
    if diametre <= 0:
        raise ValueError("Le diamètre doit être strictement positif.")
    rayon = diametre / 2
    return math.pi * rayon ** 2

def prix_par_cm2(prix, surface):
    """Renvoie le prix d'un centimètre carré."""
    if prix < 0 or surface <= 0:
        raise ValueError("Le prix doit être positif ou nul et la surface positive.")
    return prix / surface

def analyser_pizzas(pizzas):
    """Ajoute surface et prix au cm², puis classe les pizzas."""
    resultats = []
    for pizza in pizzas:
        surface = surface_pizza(pizza["diametre"])
        resultats.append({
            "nom": pizza["nom"],
            "diametre": pizza["diametre"],
            "prix": pizza["prix"],
            "surface": surface,
            "prix_cm2": prix_par_cm2(pizza["prix"], surface),
        })
    return sorted(resultats, key=lambda element: element["prix_cm2"])

def construire_rapport(pizzas):
    resultats = analyser_pizzas(pizzas)
    lignes = [
        "COMPARAISON DE PIZZAS",
        "Hypothèses : pizzas circulaires, prix d'exemple et surface seule prise en compte.",
        "",
        f"{'Taille':<12}{'Diamètre':>12}{'Prix':>10}{'Surface':>14}{'Prix/cm²':>14}",
        "-" * 62,
    ]
    for p in resultats:
        lignes.append(
            f"{p['nom']:<12}{p['diametre']:>9.1f} cm{p['prix']:>9.2f} €"
            f"{p['surface']:>11.2f} cm²{p['prix_cm2']:>11.4f} €"
        )
    meilleure = resultats[0]
    lignes += [
        "",
        f"Meilleur prix au cm² : {meilleure['nom']} ({meilleure['prix_cm2']:.4f} €/cm²).",
        "",
        "EXPERIENCE : DOUBLER LE DIAMETRE",
        f"Surface pour 20 cm : {surface_pizza(20):.2f} cm²",
        f"Surface pour 40 cm : {surface_pizza(40):.2f} cm²",
        f"Rapport des surfaces : {surface_pizza(40) / surface_pizza(20):.2f}",
        "Le diamètre est multiplié par 2, mais la surface est multipliée par 4.",
        "",
        "PRECISION DES FLOTTANTS",
        f"Calcul de pi * 13² : {surface_pizza(26):.15f}",
        f"Ecart après arrondi à 2 décimales : {abs(surface_pizza(26) - round(surface_pizza(26), 2)):.15f} cm²",
    ]
    return "\n".join(lignes) + "\n"

def main():
    rapport = construire_rapport(PIZZAS)
    print(rapport)
    chemin = Path(__file__).with_name("results.txt")
    chemin.write_text(rapport, encoding="utf-8")
    print(f"Résultats enregistrés dans : {chemin}")

if __name__ == "__main__":
    main()
