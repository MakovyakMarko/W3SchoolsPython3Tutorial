# поліморфізм означає "багато форм", і в програмуванні воно відноситься
# до методів/функцій/операторів з однаковою назвою, які можуть бути
# виконані для багатьох об'єктів або класів. Прикладом фунуції Python,
# яку можна використовувати для різних об'єктів є функція len()
x = "Hello world"
print(len(x))

mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(len(thisdict))

# поліморфізм часто використовується в методах класу, де ми можемо мати
# кілька класів з однаковою назвою методу. Наприклад, скажімо, у нас є
# три класи: Car, Boat i Plaine, і всі вони мають метод під назвою move():
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")
# через поліморфізм ми можемо виконати той самий метод для всіх
# трьох класів через цикл for
for x in (car1,boat1,plane1):
    x.move()
# А ось приклад щодо класів з дочірніми класами. Ми можемо використати
# поліморфізм там. Якщо ми використаємо наведений вище приклад і створимо
# батьківський клас Vehicle, і створимо Car,Boat,Plane дочірні класи для
# Vehicle, дочірні клами успадкують Vehicle методи та можуть замінити їх.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail!")
class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
# у прикладі вище ви бачите, що Car клас порожній, але він успадковує
# brand, model, move() від Vehicle. Класи Boat i Plane також успадковують
# brand, model, move() від Vehicle, але обидва замінюють move() метод.
# Через поліморфізм ми можемо виконувати той самий метод для всіх класів.
