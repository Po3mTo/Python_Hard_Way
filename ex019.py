# Na tym opiera się całe ćwiczenie. Mamy zdefiniowane cheese_and_crackers z dwoma wartościami. Te wartości są puste.
# Poniżej wydrukowane są zdania, które należy wydrukować w dobrym rzędzie(nie od początku tylko pod cheese_and_crackers)
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man that's enough for a party")
    print("Get a blanket.\n")



print("We can just give the function numbers directly:")
# Tutaj nadajemy wartość naszym zmiennym, czyli 20 i 30.
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# w tych 2 kolejnych liniach dajemy wartość obydwum zmiennym
amount_of_cheese = 10
amount_of_crackers = 50
# podstawa tj. cheese_and_crackers zostaje, ale zmieniają się nam wartości, które są dodawane do zdania.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")

cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# ta linia łączy liczby z zmiennymi amount_of_cheese itd. dodatkowo nasza zdefiniowana
# cheese_and_crackers to stała, która zawsze jest drukowana
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


print("The next thing we can do is to multiple our variables: ")
cheese_and_crackers(amount_of_cheese * 2, amount_of_crackers * 5)

liczba_serów = 44
liczba_krakersów = 365
paczka_krakersów = 30
paczka_serów =6

print("I add new variables and place them to the main sentences: ")
cheese_and_crackers(liczba_serów, liczba_krakersów)

print("Let's add to our packet of cheese and crackers some more packages: ")
cheese_and_crackers(paczka_serów + 22, paczka_krakersów + 2222)
