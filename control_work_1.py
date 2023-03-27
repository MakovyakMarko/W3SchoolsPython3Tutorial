
def comparison():
    x = int(input("Введіть х: "))
    y = int(input("Введіть у: "))
    if x > y:
        print("x > y")
    elif x < y:
        print("x < y")
    elif x == y:
        print("x = y")
# comparison()

line = "Hello, my name is Marko!"
if "Marko" in line:
    print("Yes, name is Marko")
else:
    print("Name is not Marko")

x = 20
y = 10
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x // y)
print(x % y)

print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print(x == y)
print(x != y)

x += 5
print(x)
x -= 5
print(x)
x *= 2
print(x)
x /= 2
print(x)
x %= 6
print(x)

list = ["Yellow","Green", "Blue"]
def myfunc():
    for x in list:
        x = input("Enter data to list: ")
        list.append(x)
        print(list)
        y = input("Would you enter more data?(y/n): ")
        if y == "y":
            myfunc()
        elif y == "n" :
            list.
            z = print(list)
        break
myfunc()