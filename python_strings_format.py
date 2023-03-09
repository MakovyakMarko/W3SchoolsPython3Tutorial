# метод format приймає передані аргументи, форматує їх
# і розміщує в рядку, де {} знаходяться заповнювачі
age = 32
txt = "My name is Marko, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder1 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder1.format(quantity, itemno, price))