# Préparation Python avant Django  
**Semaine intensive — 10 au 14 décembre 2025**

Ce dépôt contient 7 exercices.  
Chaque exercice contient exactement 2 mini-exercices très courts et précis à réaliser.  
Règles Git obligatoires :  
- Branche : ex1-les-bases, ex2-boucles, …  
- Fichiers clairement nommés (uniquement des fichiers .py, pas de HTML ou autre)  
- Pull Request + merge + tag à la fin de chaque exercice

### ex1-les-bases  
Branche : ex1-les-bases  
Fichier : ex1_les_bases.py

1. Demander un entier à l’utilisateur.  
   → S’il est positif → afficher "positif"  
   → S’il est négatif → afficher "négatif"  
   → S’il est zéro → afficher "zéro"  
   → Sinon (pas un nombre) → afficher "Ce n’est pas un nombre valide" (utiliser try/except pour gérer l’erreur)

2. Demander une note sur 20.  
   → Si note ≥ 16 → "Très bien"  
   → 14-15 → "Bien"  
   → 12-13 → "Assez bien"  
   → 10-11 → "Moyen"  
   → < 10 → "Insuffisant"  
   (Utiliser if/elif/else et input() avec conversion en float)

### ex2-boucles  
Branche : ex2-boucles  
Fichier : ex2_boucles.py

1. Avec une boucle while : demander des nombres jusqu’à taper "stop".  
   À la fin afficher le nombre de valeurs saisies, la somme et la moyenne.  
   (Gérer les entrées non numériques avec try/except)

2. Avec une boucle for : afficher la table de multiplication de 7 (7 × 1 = 7 … 7 × 10 = 70).  
   (Utiliser range() et formatage de chaînes pour un affichage propre)

### ex3-fonctions  
Branche : ex3-fonctions  
Fichier : ex3_fonctions.py

1. Créer une fonction est_pair(n) qui retourne True si n est pair, False sinon (sans if, utiliser modulo %).  
   Tester avec plusieurs valeurs.

2. Créer une fonction saluer(prenom, civilite="M.") qui retourne  
   → "Bonjour M. Dupont" ou "Bonjour Mme Durand".  
   (Utiliser des paramètres par défaut et f-strings)

### ex4-listes-dictionnaires  
Branche : ex4-listes-dictionnaires  
Fichier : ex4_listes_dictionnaires.py

1. Créer une liste de 5 fruits.  
   Ajouter un fruit avec input(), supprimer un fruit avec input(), afficher la liste triée.  
   (Utiliser .append(), .remove(), sorted())

2. Créer une liste de 3 contacts :  
   [{"nom": "Alice", "tel": "0601020304"}, …]  
   Afficher uniquement les noms, puis rechercher un contact par nom.  
   (Utiliser boucles for, if, et .get() pour les dictionnaires)

### ex5-poo  
Branche : ex5-poo  
Fichiers : voiture.py + ex5_demo.py

1. Créer une classe Voiture avec attributs marque, modele, annee, kilometrage  
   et méthode afficher() qui montre toutes les infos.  
   (Utiliser __init__ et self pour les attributs)

2. Créer une classe VoitureElectrique qui hérite de Voiture  
   et ajoute un attribut autonomie + méthode afficher() qui montre aussi l’autonomie.  
   (Utiliser super() pour l’héritage et overriding de méthodes)

### ex6-fichiers-exceptions  
Branche : ex6-fichiers-exceptions  
Fichier : ex6_journal.py

1. Écrire 5 lignes dans un fichier notes.txt (une note par ligne).  
   Puis relire le fichier et afficher uniquement les notes ≥ 10.  
   (Utiliser with open() en mode 'w' et 'r', et float() pour conversion)

2. Créer une fonction diviser(a, b) qui gère ZeroDivisionError  
   et ValueError (si a ou b n’est pas un nombre) et retourne un message clair.  
   (Utiliser try/except/else/finally pour une gestion complète)

### ex7-modules-imports  
Branche : ex7-modules-imports  
Fichiers : utils.py + ex7_demo.py

1. Dans utils.py : créer une fonction calcul_moyenne(liste) et une fonction trier_liste(liste).  
   Dans ex7_demo.py : importer et utiliser ces fonctions sur une liste de notes.

2. Créer un petit menu interactif dans ex7_demo.py qui utilise les fonctions importées :  
   → Option 1 : ajouter une note  
   → Option 2 : calculer moyenne  
   → Option 3 : trier et afficher  
   (Utiliser import from et une boucle while pour le menu)

### 3 Projets finaux à réaliser  
**Ces 3 projets doivent intégrer TOUS les concepts vus (bases, boucles, fonctions, listes/dictionnaires, POO, fichiers, exceptions, modules).**  
**Chaque projet dans une branche séparée, avec uniquement des fichiers .py (pas de HTML).**  
**Objectif : consolider tout ce qui a été appris pour être prêt à Django.**

**Projet 1 : Système de gestion de livres**  
Branche : projet1-gestion-livres  
Fichiers : livre.py (classes), gestion.py (logique principale), data.json (pour persistance)  

- Créer une classe Livre (attributs : titre, auteur, annee, disponible=True).  
- Créer une classe Bibliotheque qui gère une liste de livres (ajouter, supprimer, emprunter, rendre).  
- Utiliser des dictionnaires pour stocker les infos, des boucles pour menus, des fonctions avancées (*args pour ajouter plusieurs livres), des fichiers JSON pour sauvegarder/charger la bibliothèque.  
- Gérer exceptions (livre non trouvé, etc.).  
- Menu console : 1. Ajouter livre 2. Lister disponibles 3. Emprunter 4. Quitter et sauvegarder.

**Projet 2 : Calculatrice avancée**  
Branche : projet2-calculatrice  
Fichier : calculatrice.py  

- Créer au moins 8 fonctions : addition, soustraction, multiplication, division, puissance, racine carrée, modulo, factorielle.  
- Utiliser POO : classe Calculatrice avec méthodes pour chaque opération.  
- Menu interactif avec boucle while, input() pour choix et nombres.  
- Gérer exceptions (division par zéro, entrées invalides).  
- Sauvegarder l’historique des calculs dans un fichier log.txt (avec datetime pour timestamps).  
- Bonus : utiliser *args pour opérations sur plusieurs nombres (ex: somme de liste).

**Projet 3 : Gestionnaire de tâches (Todo List améliorée)**  
Branche : projet3-todo-list  
Fichiers : tache.py (classes), app.py (principale), tasks.json (persistance)  

- Créer une classe Tache (attributs : description, priorite, completee=False, date_creation).  
- Créer une classe GestionTaches qui gère une liste de tâches (ajouter, marquer complète, supprimer, trier par priorité).  
- Utiliser dictionnaires pour priorités, compréhensions pour filtrer (tâches incomplètes), modules pour séparer code.  
- Fichiers JSON pour charger/sauvegarder.  
- Menu console avec boucles, fonctions lambda pour tri, exceptions pour erreurs utilisateur.  
- Intégrer tout : bases, structures de données, POO, fichiers, etc.

Quand les 7 exercices + 3 projets sont terminés et mergés, tu maîtrises réellement tout le Python nécessaire pour Django !

Bonne semaine et bon code !
