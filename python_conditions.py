a = 33
b = 200
if b > a:
    print("b is greater than a")

if b > a:
    print("b is greater than a")
elif a==b:
    print("a nad b are equal")

if b > a:
    print("b is greater than a")
elif a==b:
    print("a nad b are equal")
else:
    print("a is greater than b")
# якщо є один оператор для виконання ви можете розмістити все в одному рядку
if a < b: print("b is greater than a")
# якщо є тільки один оператор для виконення, один для if і один для else, ви
# можете розмістити їх в одному рядку
print("A") if a > b else print("B")
a1 = 330
b1 = 330
print("A") if a1 > b1 else print("=") if a1 == b1 else print("B")

# ключове слово and є логічним оператором, використовується для
# комбінування умовних оператороів
a2 = 200
b2 = 33
c2 = 500
if a2 > b2 and c2 > a2:
    print("Both conditions are True")
# ключове слово or є лог-м оператотром і використовується
# для комбінування умовних операторів
if a2 > b2 or a2 > c2:
    print("At least one of the conditions is True")
# not використовується для зворотного результату умовного оператора
if not a2 > b2:
    print("a is NOT greater than b")
else:
    print("b is NOT greater than a")

# можна вкладати if оператори всередину if оператороів, вони називються вкладеними
x = 41
if x > 10:
    print("Above ten, ")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# якщо if операторо без змісту, вставте pass щоб уникнути помилки
y = 42
if x > y:
    pass
