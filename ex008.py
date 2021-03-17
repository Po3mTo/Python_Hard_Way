formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# This example is a little bit harder, but it's clear.
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I like ice creams, and pancakes.",
    "Also I found my new passion (probably). And you'll never believe what it is...",
    "It's programming.",
    "Pretty good as a boy who do not know math."
))
# Good tool to work faster. It wasn't in the scrimba course.
# Jak to działa? Co przez to daję znać komputerowi?
# 1. Weź łańcuch formatyzatora zdefiniowany w linii 1.
# 2. Wywołaj jego funkcję formatowania, co jest podobne do powiedzenia mu, aby wykonał polecenie wiersza poleceń o nazwie format.
# 3. Przekaż do formatu cztery argumenty, które odpowiadają czterem {} w zmiennej formatter.
# Jest to podobne do przekazania argumentów do polecenia wiersza poleceń format.
# 4. Wynikiem wywołania formatu na formatterze jest nowy łańcuch, który ma {} zastąpione czterema zmiennymi.
# To jest właśnie to, co drukuje teraz 'print'.
