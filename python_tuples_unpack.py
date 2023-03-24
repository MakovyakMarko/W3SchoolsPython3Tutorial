fruits = ("apple", "banana", "cherry")
print(fruits)
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# кіл-ть змінних має збігатись з кіл-тю ел-в кортежу, якщо
# ні, то треба використовувати * для того, щоб зібрати останні в список
fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits1
print(green)
print(yellow)
print(red)
# якщо * призначити не останній змінній, то Python призначатиме значення
# змінній, доки кіл-ть значень, що залишиться не збігатиметься з кіл-тю змінних, які залишились
fruits2 = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits2
print(green)
print(tropic)
print(red)
