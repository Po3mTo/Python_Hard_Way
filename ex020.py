from sys import argv

script, input_file = argv
# f to plik, który załączamy. W tym wypadku jest to test.txt
# definiujemy, że print_all(f(czyli nasz plik, bo jest to w nawiasie)). Dajemy mu funkcję, by przeczytał nam cały plik.
def print_all(f):
    print(f.read())
# znowu definiujemy rewind(f), by szukał w pliku f początku. seek działa w bytes, więc seek(0) oznacza niezależnie od której linii zaczniemy pisać, to on zacznie od pierwszego bita.
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    #readline() - wewnątrz nawiasu znajduje się kod, który skanuje k
    print(line_count, f.readline())
# dajemy funkcję current_file, by otworzyła plik, który wpisujemy przy włączaniu programu (test.txt).
current_file = open(input_file)

print("First let's print the whole file:\n")
# zdefiniowane print_all powoduje, że odpalamy plik i czytamy tego umieszczonego w nawiasie.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# zdefiniowane rewind odpowiada za szukanie od pierwszego bita w kodzie (seek(0).
rewind(current_file)

print("Let's print three lines:")
current_line = 1
# zdefiniowane print_a_line(current_line(1), current_file(open(input_file = test.txt)))
print_a_line(current_line, current_file, end = '')
# ta sama sytuacja tylko dodajemy do current_line + 1
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
