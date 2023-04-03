# json - це синтаксис для зберігання та обміну данними
# json - це текст, написаний за допомогою нотації об'єктів JavaScript
import json
# якщо у вас є рядок json, ви можете проаналізувати його за
# допомогою json.loads() методу
x = '{"name":"Marko", "age":32, "city":"Kyiv"}'
y = json.loads(x)
print(y["city"])

x = {
    "name":"Marko",
    "age":32,
    "city":"Kyiv"
}
y = json.dumps(x)
print(y)

# перетворіть об'єкти python на рядки json і надрукуйте значення
print(json.dumps({"name":"Marko", "age":32}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(12.234))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# перетворіть об'єкт python, що містить усі допустимі типи даних
z = {
    "name": "Marko",
    "age":32,
    "married":True,
    "divorced":False,
    "children":("Ann","Billy"),
    "pets":None,
    "cars":[
        {"model":"BMW Z4", "mpg": 27.5},
        {"model":"Mercedes", "mpg": 24.1}
    ]
}
print(json.dumps(z))
# json.dumps() має параметри, які полегшують читання результату
print(json.dumps(z, indent=4))
# також можна встановити роздільники, які за замовчанням (", ",": ")
# Використовуйте separators параметр, щоб змінити стандартний роздільник
print(json.dumps(z, indent=4, separators=(". "," = ")))
print(json.dumps(z, indent=4, sort_keys=True))