from datetime import datetime
import math

date = datetime.now()

class Calculatrice:
    

    def __init__(self, fichier_log="log.txt"):
       
        self.fichier_log = fichier_log

    def _sauvegarder(self, operation, resultat):
        
       
        with open(self.fichier_log, "a") as fichier:
            fichier.write(f"{date} - {operation} = {resultat}\n")

   
    def addition(self, *args):
        resultat = sum(args)
        self._sauvegarder(f"Addition {args}", resultat)
        return resultat

    def soustraction(self, a, b):
        resultat = a - b
        self._sauvegarder(f"{a} - {b}", resultat)
        return resultat

    def multiplication(self, *args):
        resultat = 1
        for n in args:
            resultat *= n
        self._sauvegarder(f"Multiplication {args}", resultat)
        return resultat

    def division(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Il est impossible de diviser un nombre par zero")
        resultat = a / b
        self._sauvegarder(f"{a} / {b}", resultat)
        return resultat

    def puissance(self, a, b):
        resultat = a ** b
        self._sauvegarder(f"{a} ^ {b}", resultat)
        return resultat

    def racine_carree(self, a):
        if a < 0:
            raise ValueError("Nombre négatif")
        resultat = math.sqrt(a)
        self._sauvegarder(f"√{a}", resultat)
        return resultat

    def modulo(self, a, b):
        resultat = a % b
        self._sauvegarder(f"{a} % {b}", resultat)
        return resultat

    def factorielle(self, a):
        
        if a < 0:
            raise ValueError("Impossible nombre négatif")
        resultat= 1
        while a > 0 :
           resultat *= a
           a-=1
        self._sauvegarder(f"{a}!", resultat)
        return resultat




def affichage_du_menu():
    print("\n--- CALCULATRICE NIVEAU AVANCE  ---")
    print("1-Addition (plusieurs nombres)")
    print("2- Soustraction")
    print("3- Multiplication (plusieurs nombres)")
    print("4- Division")
    print("5- Puissance")
    print("6- Racine carrée")
    print("7- Modulo")
    print("8- Factorielle")
    print("0- Quitter")


def main():
    calc = Calculatrice()

    while True:
        affichage_du_menu()
        choix = input("Choisissez une option : ")

        try:
            if choix == "1":
                nums = list(map(float, input("Nombres : ").split()))
                print("Résultat :", calc.addition(*nums))

            elif choix == "2":
                a = float(input("a = "))
                b = float(input("b = "))
                print("Résultat :", calc.soustraction(a, b))

            elif choix == "3":
                nums = list(map(float, input("Nombres : ").split()))
                print("Résultat :", calc.multiplication(*nums))

            elif choix == "4":
                a = float(input("a = "))
                b = float(input("b = "))
                print("Résultat :", calc.division(a, b))

            elif choix == "5":
                a = float(input("a = "))
                b = float(input("b = "))
                print("Résultat :", calc.puissance(a, b))

            elif choix == "6":
                a = float(input("Nombre : "))
                print("Résultat :", calc.racine_carree(a))

            elif choix == "7":
                a = float(input("a = "))
                b = float(input("b = "))
                print("Résultat :", calc.modulo(a, b))

            elif choix == "8":
                a = int(input("Nombre entier : "))
                print("Résultat :", calc.factorielle(a))

            elif choix == "0":
                print("Au revoir")
                break

            else:
                print("Choix invalide.")

        except ValueError:
            print("Erreur : entrée invalide.")

        except ZeroDivisionError:
            print("Erreur : division par zéro.")

        finally:
            print("Opération terminée.")


if __name__ == "__main__":
    main()
