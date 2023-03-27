class MyClass:
    x = 5
print(MyClass)
p1 = MyClass()
print(p1.x)
# використовуйте функцію __init__(), щоб призначити значення властивостям
# об'єкта або іншим операціям, які необхідно виконувати під час створення
# об'єкта:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# функція __init__() викликається автоматично кожного разу, коли клас ви
p2 = Person("Marko", 32)
print(p2.name)
print(p2.age)
