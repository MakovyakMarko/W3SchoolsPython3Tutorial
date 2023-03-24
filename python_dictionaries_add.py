thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# додати елемент до словника можна за допомогою
# нового ключа індексу та призначення йому значення
thisdict["color"] = "red"
print(thisdict)
# або через метод update()
thisdict.update({"owner": "Marko"})
print(thisdict)