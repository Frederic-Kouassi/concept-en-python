contacts = [
    {"nom": "Alice", "tel": "0601020304"},
    {"nom": "Bob", "tel": "0602030405"},
    {"nom": "Charlie", "tel": "0603040506"}
]
print("Liste des noms :")
for contact in contacts:
    print(contact.get("nom"))

recherche = input("Entrez le nom à rechercher : ")
trouve = False
for contact in contacts:
    if contact.get("nom") == recherche:
        print(f"Contact trouvé : {contact}")
        trouve = True
        break

if not trouve:
    print("Contact non trouvé.")
