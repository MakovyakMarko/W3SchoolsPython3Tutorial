print(10 > 9)
print(10 == 9)
print(10 < 9)

#a = int(input("Введіть значення для а: "))
#b = int(input("Введіть значення для b: "))
#if b > a:
#    print("b більше від a")
#else:
#    print("b менше від a")

#оцініть значення, функція bool надасть значення true або false
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print(bool(""))
print(bool("abc"))
print(bool(0))
print(bool(123))
print(bool([]))
print(bool(["apple", "banana", "cherry"]))
print(bool(False))
print(bool(None))
print(bool(()))
print(bool({}))

#якщо __len__ повертає 0, то значення bool=false,
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

# можна створювати функції, які повертають логічне значення
def myFunction():
    return True
print(myFunction())
# ви можете створювати код на основі булевої відповіді функції
if myFunction():
    print("YES!")
else:
    print("NO!")

x1 = 200
print(isinstance(x, int))