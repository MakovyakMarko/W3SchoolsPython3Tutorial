class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("Marko","Makovyak")
x.printname()

class Student(Person):
    pass
y = Student("Marko", "Makovyak")
y.printname()

class Student1(Person):
    # коли додається функція __init__(), дочірній клас більше
    # не успадковує батьківську __init__() функцію.
    # функція __init__() дочірнього класу перекриває успадкування
    # функції батьківського класу. Щоб зберегти успадкування додайте
    # виклик до батьківської функції __init__():
    def __init__(self,fname,lname,year):
        #Person.__init__(self, fname, lname)
    # функція super(), змусить дочірній клас успадковувати всі методи
    # та властивості свого батька
        super().__init__(fname, lname)
    # використовуючи функцію super(), вам не потрібно використовувати
    # ім'я батьківського елемента, він автоматично успадковує матоди
    # та властивості свого батька
        self.graduationyear = year
z = Student1("Marko", "Makovayak", 2012)
print(z.graduationyear)

class Student2(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    # якщо ви додаєте метод до дочірнього класу з тим же ім'ям, що й функція
    # в батьківському класі, успадкування методу буде перевизначено.
z = Student2("Marko", "Makovyak", 2012)
z.welcome()