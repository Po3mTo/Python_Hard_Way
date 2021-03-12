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
