thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# цикл for повертає тільки значення ключів, але також існують методи
# для повернення значень
for x in thisdict:
    print(x)
# вивести всі значення в словнику, по одному
for x in thisdict:
    print(thisdict[x])
# також можна використовувати values()
for x in thisdict.values():
    print(x)
# можна використовувати keys() для повернення ключів
for x in thisdict.keys():
    print(x)
# перегляньте ключі і значення за допомогою методу items()
for x,y in thisdict.items():
    print(x,y)
