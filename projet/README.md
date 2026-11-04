# Projet : Pizza, une histoire de géométrie et de calcul numérique

## Contexte

Quand on compare deux pizzas, on regarde souvent leur diamètre et leur prix. Pourtant, le diamètre ne donne pas directement la quantité : une pizza est un disque et sa surface dépend du carré du rayon. J'ai voulu vérifier quelle taille est la plus intéressante si l'on compare uniquement la surface obtenue pour le prix payé.

## Question de départ

Une pizza plus grande est-elle toujours plus avantageuse ? Comment évolue sa surface lorsque son diamètre augmente ?

## Démarche

1. Calculer la surface avec la formule A = pi x r².
2. Calculer le prix par cm² pour chaque taille.
3. Classer les pizzas selon ce rapport.
4. Doubler le diamètre pour observer l'évolution de la surface.
5. Afficher plusieurs décimales pour observer les nombres flottants et l'effet de l'arrondi.

Le programme utilise Python standard, sans NumPy. Les prix inscrits dans `main.py` sont des exemples fictifs destinés à tester la méthode ; ils peuvent être remplacés par des prix relevés dans un magasin.

## Résultats

Exécuter `main.py` affiche le tableau comparatif et crée `results.txt` avec la sortie complète. Les valeurs sont calculées par le programme : elles ne sont pas saisies à la main.

L'expérience sur le diamètre montre qu'une pizza de diamètre doublé possède quatre fois la surface. La meilleure offre dépend donc du prix au cm², pas seulement du diamètre ni du prix affiché.

## Analyse et limites

Le modèle suppose que les pizzas sont parfaitement circulaires et compare uniquement leur surface. Il ne tient pas compte de l'épaisseur de la pâte, de la garniture, de la qualité ni des différences de recette. Les prix sont des exemples et ne représentent pas une enquête commerciale.

Les calculs utilisent des nombres flottants. L'affichage arrondi peut masquer de très petits écarts, mais la valeur interne conserve davantage de décimales. Pour ce problème, les erreurs d'arrondi sont très faibles par rapport aux différences de surface et de prix.

## Lancer le projet

Dans PyCharm, ouvrir le dossier `projet`, puis exécuter `main.py`.

Pour lancer les tests : clic droit sur `test_projet.py` puis `Run`. Il est également possible d'utiliser `python -m unittest test_projet.py` depuis ce dossier.

## Fichiers

- `main.py` : calculs et comparaison des pizzas.
- `results.txt` : résultats d'une exécution du programme.
- `test_projet.py` : tests automatiques des fonctions principales.
- `README.md` : présentation, démarche et limites du projet.

## Utilisation d'un assistant

Une assistance par intelligence artificielle a servi à organiser le projet, proposer des tests et relire le code. Les choix de prix d'exemple, les calculs et les conclusions doivent être vérifiés et compris avant le rendu.
