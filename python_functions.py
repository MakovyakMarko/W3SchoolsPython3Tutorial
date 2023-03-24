# функція це блок коду, який виконується лише тоді, коли його викликають
def myfunc():
    print("Hello from function")
myfunc()
# Інфморацію можна передати у функцію як аргументи.
# Аргументи вказуються в душках, можна передати скільки загодно аргументів,
# просто розділивши їх комою.
def my_function(fname):
    print(fname + " Makovyak")
my_function("Marko")
my_function("Veronika")
my_function("Stepan")
# якщо в фунції вказано 2 аргументи, а ви передаєте 1 або 3 то буде
# помилка. До функції треба передавати тільки вказану кількість аргументів
def my_function(fname, lname):
    print("Hello, " + fname + " " + lname)

x = input("Enter your first name: ")
y = input("Enter your last name: ")
my_function(x,y)
# якщо ви не знаєте, скільки аргументів буде передано у функцію, додайте
# * перед назвою параметра у визначенні функції. Токим чином функція отримає
# кортеж аргументів і зможе отримати відповідний дотуп до елементів:
def my_function1(*kids):
    print("The youngest child is " + kids[2])
my_function1("Emil","Tobias", "Linus")
# можна надсилати аргументи за допомогою синтаксису ключ:значення.
# Порядок таких аргументів не має значення
def my_function2(child1, child3, child2):
    print("The youndest child is " + child3)
my_function2(child1="Tobias",child2="Linus", child3="Emil")
# якщо ви не знаєте скільки ключових аргументів буде передано у функцію,
# додайте ** (дві зірочки). Таким чином функція отримає словник аргументів
# і матиме відповідний доступ до елементів:
def my_function3(**kid):
    print("His last name is " +kid["lname"])
my_function3(fname = "Tobias", lname = "Refsnes")
# якщо добавити значення за замовчуванням і викликати функцію без аргументу,
# вона використовуватиме значення за замовчуванням:
def my_function4(country = "Ukraine"):
    print("I am from " + country)
my_function4("USA")
my_function4()
my_function4("England")
# ви можете надсилати будь-які типи даних аргументу до функції(рядок,
# число, список, словник тощо), і він буде розглядатись як той самий тип
# даних у функції. Наприклад якщо надішлите список як аргумент, він все одно
# буде списком, коли досягне функції:
def my_function5(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function5(fruits)
# щоб дозволити функції повертати значення, використовуйте return оператор:
def my_function6(x):
    return 5 * x
print(my_function6(3))
print(my_function6(5))
print(my_function6(9))

def my_calc(num1,num2):
    return  num1 + num2
num1 = int(input("Enter digit a: "))
num2 = int(input("Enter digit b: "))
print(my_calc(num1,num2))
# якщо у вас є функція без вмісту, вставте pass оператор, щоб уникнути помилки
def my_function7():
    pass
# рекурсія - поширена математична та програмна концепція. Це означає,
# що функція викликає сама себе. Перевагою цього є те, що ви можете
# переглядати дані, щоб отримати результат.
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Resulrs")
tri_recursion(6)