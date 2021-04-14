from sys import argv

script, filename = argv

print(f"""Twój plik o nazwie {filename} zostanie otwarty.\n
Jeśli nie chcesz go otwierać wybierz 'q'.\n
Jeśli natomiast chcesz otworzyć plik wybierz 'ok'.\n""")
pyt = input("A więc?: ")
if pyt == "q":
    print("ok, żegnaj!")
    plik = quit(filename)

plik = open(filename, 'w')

print("Teraz usuniemy stary zapis pliku i zaraz zastąpimy go nową treścią. Masz do dyspozycji 4 linie:")
plik.truncate()

line1 = input()
line2 = input()
line3 = input()
line4 = input()

plik.write(line1 + " " + line2)
plik.write("\n")
plik.write(line3)
plik.write("\n")
plik.write(line4)
plik.write("\n")

plik.close()
