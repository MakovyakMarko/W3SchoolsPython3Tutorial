# ітератор це об'єкт, який містить лічильну кількість значень
# ітератор в python - це об'єкт, який реалізує протокол ітератора, який
# складається з матодів __iter__() i __next__()
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# цикл for фактично створює об'єкт-ітератор і виконує метод next() для
# кожного циклу
mytuple1 = ("apple", "banana", "cherry")
for x in mytuple1:
    print(x)

mystr1 = "banana"
for x in mystr1:
    print(x)

# щоб стоворити об'єкт/клас як ітератор, вам потрібно реалізувати методи
# __iter__() та __next__() для вашого об'єкта.
# метод __iter__() дозволяє виконати деяку ініціалізацію під час створення
# об'єкта. Ви можете виконувати операції (ініціалізацію тощо), але завжди
# повинні повертати сам об'єкт ітератора. return self
# метод __next__() також дозволяє вам виконувати операції та повинен
# повертати наступний елемент у послідовності.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers1:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass1 = MyNumbers1()
myiter1 = iter(myclass1)

for x in myiter1:
    print(x)

