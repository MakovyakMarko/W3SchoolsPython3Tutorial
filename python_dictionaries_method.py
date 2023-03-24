# створіть словник із 3 ключами, усі за значенням 0
x = ("key1", "key2", "key3")
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)
# отримайте значення елемента модель
thisdict1 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = thisdict1.setdefault("model", "Bronco")
print(x)
