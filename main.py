import random

print("Welkom; raad het geheime getal!")
print("Groetjes van een hulpvaardige vriend.")
geheim = random.randint(1, 100)
gok = int(input("Doe een gok: "))
while gok != geheim:
    print("Fout!")
    gok = int(input("Probeer het nog eens: "))
print("Goed!")
