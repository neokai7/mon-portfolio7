# Analyse des ventes mensuelles de produits Lian Li

Je m’appelle Pascal, 44 ans, papa solo de trois garçons, en reconversion professionnelle vers le développement web full-stack. Passionné depuis toujours par l’informatique et le hardware, je me consacre pleinement à cette formation depuis deux mois pour devenir un développeur compétent et engagé.

---

## Énoncé du projet

Cette fonction `ventes_mensuelles_lianli` prend en entrée une liste de nombres représentant les ventes mensuelles (en nombre d’unités vendues) d’un produit de la marque Lian Li sur une année complète (12 mois).

Elle réalise une analyse simple mais complète des données :  
- Calcule le total des ventes sur l’année  
- Calcule la moyenne mensuelle des ventes  
- Identifie le mois avec les meilleures ventes ainsi que celui avec les ventes les plus faibles  
- Liste les mois où les ventes sont inférieures à la moyenne annuelle

Elle affiche ces résultats de manière lisible, en associant chaque valeur au mois correspondant (en français).

---

## Code Python

```python
from statistics import mean

def ventes_mensuelles_lianli(donnees):
    if not donnees:
        print("Aucune donnée saisie.")
        return
    
    mois_noms = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

    total_ventes = sum(donnees)
    moyenne_ventes = round(mean(donnees))
    ventes_max = max(donnees)
    ventes_min = min(donnees)
    indice_max = donnees.index(ventes_max)
    indice_min = donnees.index(ventes_min)

    mois_max = mois_noms[indice_max]
    mois_min = mois_noms[indice_min]
    mois_min_moyenne = [i for i, ventes in enumerate(donnees) if ventes < moyenne_ventes]

    print(f"Le total des ventes mensuelles Lian li est de {total_ventes} fans vendus.")
    print(f"La moyenne des ventes mensuelles Lian Li est de {moyenne_ventes} fans vendus.")
    print(f"Le meilleure mois de ventes est le mois de {mois_max} avec {ventes_max} fans vendus.")
    print(f"Le mois le plus bas est le mois de {mois_min} avec seulement {ventes_min} fans vendus.")
    print("Les mois de ventes en dessous de la moyenne sont: " + ', '.join(f"{mois_noms[i]} avec {donnees[i]} fans vendus" for i in mois_min_moyenne) + ".")
