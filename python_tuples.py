# кортеж це впорядкований, індексований, незмінний набір
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# можна дублювати значення
thistuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple1)
# щоб визначити кількіть елементів в кортежі використовується метод len
print(len(thistuple1))
# для створення кортежу з одним елементом треба в кінці добавляти кому, бо це не буде кортеж
thistuple2 = ("apple",)
print(type(thistuple2))
thistuple2 = ("apple")
print(type(thistuple2))
# елементи кортежу можуть мати будь-який тип даних
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1,2,3,4, 5)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
# кортеж може містити різні типи даних
tuple4 = ("age", 32, True, "male", 34)
print(tuple4)
# type tuple
print(type(tuple4))
# constructor
tuple5 = tuple(("apple", "banana", "cherry"))
print(tuple5)
