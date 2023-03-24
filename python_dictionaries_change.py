thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# ви можете змінити значення елемента, звернувшись до назви ключа
thisdict["year"] = 2020
print(thisdict)
# update() оновить словник елементами з заданого аргументу. Аргумент має
# бути словником  або ітерованим об'єктом із парами ключ:значення
thisdict.update({"year": 1964})
print(thisdict)
