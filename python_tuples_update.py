# котержі незмінні, але є обхідні шляхи
# можна перетворити кортеж на список, додати елемент, а потім перетворити список назад на кортеж
x = ("apple", "banana", "cherry")
print("Є tuple: ",x)
y = list(x)
y[1] = "kiwi"
print("Перетворюєм tuple y list i змінюєм елемент",y)
x = tuple(y)
print("Перетворюєм list y tuple",x)
# додати елемент можна таким самим шляхом
print(x)
y = list(x)
y.append("mango")
print(y)
x = tuple(y)
print(x)
# додати кортеж до кортежу можна так
y = ("orange",)
x += y
print(x)
# видалити елемент можна таким самим шляхом, змінити на список, а потім назад
y = list(x)
y.remove("cherry")
x = tuple(y)
print(x)
# можна видалити кортеж
del x
print(x)
