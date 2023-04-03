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
# функція __str__() контролює те, що має повертатися,
# коли об'єкт класу представлено у вигляді рядка.
# коли рядкова функція __str__() не встановлена,
# повертається рядкове представлення об'єкта
print(p2)

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p3 = Person1("Marko",32)
print(p3)

# методи в об'єктах - це функції, які належать об'єкту.
class Person2:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p4 = Person2("Marko", 32)
p4.myfunc()

# параметр self є посиланням на поточний екземпляр класу та
# використовується для доступу до змінних, які належать до класу
# його не обов'язково називати self, ви можете назвати цей
# параметр як завгодно, але він має бути першим парамертром
# будь-якої фунеції в класі
class Person3:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name + ". And i am " + str(abc.age))
p5 = Person3("Marko", 32)
p5.myfunc()

# змінити властивості об'єкта можна таким чином:
p5.age = 18
print(p5.age)
# видалити властивості об'єкта можна таким чином:
del p5.age
# можна видалити об'єкт за допомогою del ключового слова:
del p5
# якщо є клас визначення без змісту, треба використовувати pass,
# щоб уникнути помилки
class Person4:
    pass
