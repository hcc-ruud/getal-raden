import random

print("Welkom; raad het geheime getal!")
print("Jammer vriend, ik was hier eerst.")
geheim = random.randint(1, 100)
gok = int(input("Doe een gok: "))
while gok != geheim:
    print("Fout!")
    gok = int(input("Probeer het nog eens: "))
print("Goed!")
