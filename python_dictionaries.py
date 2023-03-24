# словники використовуються для зберігання данних у парах ключ:значення
# словник це збірка, яка є впорядкованою, змінюваною, та не допускає дублікатів
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
# на елемент можна посилатись через ім'я ключа
print(thisdict["brand"])
# в словнику не може бути двох елементів з однаковим ключем. Повторні
# значення перезапишуть існуючі
thisdict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict1)
# щоб визначити скільки елементів є в словнику треба використати метод len
print(len(thisdict1))
# словники можуть містити будь-які типи даних
thisdict2 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict2)
print(type(thisdict2))
# constructor dict()
thisdict3 = dict(name = "John", age = 32, country = "Norway")
print(thisdict3)
