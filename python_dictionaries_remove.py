thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# popitem() видаляє останній встановлений елемент
# (у версіях до 3.7 видаляється випадковий елемент)
thisdict.update({"model": "Mustang"})
print(thisdict)
thisdict.popitem()
print(thisdict)
# ключове слово del може видалити елемент із вказаною назвою ключа
del thisdict["year"]
print(thisdict)
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# clear() очищає словник
thisdict.clear()
print(thisdict)
# також del може повністю видалити словник
del thisdict
print(thisdict)
