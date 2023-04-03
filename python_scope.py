# локальна змінна:
def myfunc():
    x = 300
    print(x)
myfunc()
# локальну змінну можна використовувати у вкладених в функцію функціях
def myfunc1():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc1()

x = 300
def myfunc2():
    print(x)
myfunc2()
print(x)
# якщо є дві змінних локальна і глобальна, але з однією назвою, то це
# різні змінні
x = 300
def myfunc3():
    x = 200
    print(x)
myfunc3()
print(x)
# оголошуєм локальну змінну глобальною
def myfunc4():
    global y
    y = 400
myfunc4()
print(y)
# змінюєм глобальну змінну в локальній функції
z = 500
def myfunc5():
    global z
    z = 550
print(z)
myfunc5()
print(z)
