thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# можна отримати доступ до елемента через ключ
x = thisdict["model"]
print(x)
# той самий результат дасть метод get()
x1 = thisdict.get("model")
print(x1)
# keys() поверне список усіх ключів у словнику
x2 = thisdict.keys()
print(x2)
# додайте новий елемент до оригінального словника та подивіться,
# що список ключів також оновлюється:
thisdict["color"] = "white"
print(x2)
# values() поверне список усіз значень у словнику
x3 = thisdict.values()
print(x3)
# внесіть зміни в оригінальний словник і перевонайтесь,
# що список значень також оновлюється:
thisdict["year"] = 2020
print(x3)
# додаючи елемент до словника, ми також можем переглянути оновлений список значень
thisdict["wheels"] = 4
print(x2)
print(x3)
# items() поверне кожен елемент у словнику як кортежі у списку
x4 = thisdict.items()
print(x4)
# після внесення змін, вони будуть відображені в списку елементів
thisdict["year"] = 1964
print(x4)
# після додавання елементів список також оновлюється
thisdict["owner"] = "Marko"
print(x4)
# перевірте чи існує ключ
if "owner" in thisdict:
    print("Yes, this car has owner")
