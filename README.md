# Préparation Python avant Django  
**Semaine intensive — 10 au 14 décembre 2025**

Ce dépôt contient 7 exercices.  
Chaque exercice contient exactement 2 mini-exercices très courts et précis à réaliser.  
Règles Git obligatoires :  
- Branche : ex1-les-bases, ex2-listes, …  
- Fichiers clairement nommés  
- Pull Request + merge + tag à la fin de chaque exercice

### ex1-les-bases  
Branche : ex1-les-bases  
Fichier : ex1_les_bases.py

1. Demander un entier à l’utilisateur.  
   → S’il est positif → afficher "positif"  
   → S’il est négatif → afficher "négatif"  
   → S’il est zéro → afficher "zéro"  
   → Sinon (pas un nombre) → afficher "Ce n’est pas un nombre valide"

2. Demander une note sur 20.  
   → Si note ≥ 16 → "Très bien  
   → 14-15 → Bien  
   → 12-13 → Assez bien  
   → 10-11 → Moyen  
   → < 10 → Insuffisant

### ex2-boucles  
Branche : ex2-boucles  
Fichier : ex2_boucles.py

1. Avec une boucle while : demander des nombres jusqu’à taper "stop".  
   À la fin afficher le nombre de valeurs saisies, la somme et la moyenne.

2. Avec une boucle for : afficher la table de multiplication de 7 (7 × 1 = 7 … 7 × 10 = 70)

### ex3-fonctions  
Branche : ex3-fonctions  
Fichier : ex3_fonctions.py

1. Créer une fonction est_pair(n) qui retourne True si n est pair, False sinon (sans if).

2. Créer une fonction saluer(prenom, civilite="M.") qui retourne  
   → "Bonjour M. Dupont" ou "Bonjour Mme Durand"

### ex4-listes-dictionnaires  
Branche : ex4-listes-dictionnaires  
Fichier : ex4_listes_dictionnaires.py

1. Créer une liste de 5 fruits.  
   Ajouter un fruit avec input(), supprimer un fruit avec input(), afficher la liste triée.

2. Créer une liste de 3 contacts :  
   [{"nom": "Alice", "tel": "0601020304"}, …]  
   Afficher uniquement les noms, puis rechercher un contact par nom.

### ex5-poo  
Branche : ex5-poo  
Fichiers : voiture.py + ex5_demo.py

1. Créer une classe Voiture avec attributs marque, modele, annee, kilometrage  
   et méthode afficher() qui montre toutes les infos.

2. Créer une classe VoitureElectrique qui hérite de Voiture  
   et ajoute un attribut autonomie + méthode afficher() qui montre aussi l’autonomie.

### ex6-fichiers-exceptions  
Branche : ex6-fichiers-exceptions  
Fichier : ex6_journal.py

1. Écrire 5 lignes dans un fichier notes.txt (une note par ligne).  
   Puis relire le fichier et afficher uniquement les notes ≥ 10.

2. Créer une fonction diviser(a, b) qui gère ZeroDivisionError  
   et ValueError (si a ou b n’est pas un nombre) et retourne un message clair.

### ex7-projet-final  
Branche : ex7-projet-final  
Fichiers libres (peu importe le nombre)

Créer une petite application console « Todo List » qui permet de :
1. Ajouter une tâche
2. Voir toutes les tâches
3. Marquer une tâche comme terminée
4. Sauvegarder/quitter → les tâches sont enregistrées dans un fichier todos.json  
   et rechargées au démarrage

Quand les 7 exercices (14 mini-exercices + le projet) sont terminés et mergés, tu es 100 % prêt pour Django !

Bonne semaine et bon code !
