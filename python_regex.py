# регулярний вираз - це послідовність символів, яка формує шаблон пошуку.
# Регулярний вираз можна використовувати, щоб перевірити, чи рядок містить
# указаний шаблон пошуку. Для початку треба імпортувати пакет re для роботи
# з регулярними виразами
import re
# провірте рядок, щоб побачити, чи починається він на "The" і закінчується
# на "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("YES! We have a match!")
else:
    print("No match")

# знайти всі букви алфавіту в нижньому регістрі між "a" i "m":
x = re.findall("[a-m]",txt)
print(x)
# знайти всі цифри
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)
# знайти послідовність яка починається на "he" потім слідують два будь-які
# символи а потім йде "о"
txt = "hello planet"
x = re.findall("he..o", txt)
print(x)
# провірити чи рядок починається на hello
x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")
# провірити чи рядок закінчується на planet
x = re.findall("planet$", txt)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")
# знайти послідовність, яка починається на "he", потім слідує 0 або більше
# будь-яких символів, а потім йде "о"
x = re.findall("he.*o", txt)
print(x)
# знайти послідовність, яка починається на "he", потім слідує 1 або більше
# будь-яких символів, а потім йде "o"
x = re.findall("he.+o", txt)
print(x)
# знайти послідовність, яка починається на "he", потім слідує 0 або 1
# будь-який символ, а потім йде "о"
x = re.findall("he.?o", txt)
print(x)
# знайти послідовність, яка починається на "he", потім слідує конкретно 2
# будь-які символи, а потім йде "о"
x = re.findall("he.{2}o", txt)
print(x)
# провірити чи рядок має хочаб одне з спіпадінь, або "fals" або "stays"
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
    print("Yes, there is at least one match")
else:
    print("No match")
# повертає співпадіння якщо символи знаходять на початку рядка
txt = "The rain in Spain"
x = re.findall("\AThe", txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("No match")
# повертає співпадіння де символи на початку слова. r добавлено для того, щоб бути впевненим що
# рядок розглядається як необроблений рядок
x = re.findall(r"\bain", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає співпадіння де символи на в кінці слова
x = re.findall(r"ain\b", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає співпадіння якщо символи не на початку слова
x = re.findall(r"\Bain", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає співпадіння якщо символи не на кінці слова
x = re.findall(r"ain\B", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає співпадіння, якщо в рядку є цифри
x = re.findall("\d", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає співпадіння, якщо в рядку немає цифр
x = re.findall("\D", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає співпадіння, там де в рядку є пробіли
x = re.findall("\s", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає співпадіння, там де в рядку немає пробілів
x = re.findall("\S", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає співпадіння там де в рядку є слова
x = re.findall("\w", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає співпадіння там, де в рядку немає слів
x = re.findall("\W", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає співпадіння, коли символи є в кінці рядка
x = re.findall("Spain\Z", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# set пошук в рядку набору символів
# повертає збіг там в рядку є вказані символи
x = re.findall("[arn]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає збіг там де в рядку є якісь з вказаного діапазону символів
x = re.findall("[a-n]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає збіг для любого символа за винятком вказаних
x = re.findall("[^arn]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає збіг де люба з цифр присутня
x = re.findall("[0123]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
#
# повертає збіг де в рядку присутня люба цифра з вказаного діапазону
txt1 = "8 times before 11:45 AM"
x = re.findall("[0-9]", txt1)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає збіг де рядок має два символи між 00 та 59
x = re.findall("[0-5][0-9]", txt1)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# повертає збіг де любий з символів з вказаного діапазону присутній (для символів нижнього
# і верхнього регістрів)
x = re.findall("[a-zA-Z]", txt1)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# в наборах операції над цифрами не мають спеціального значення, тому повертається збіг, якщо
# в рядку є +
x = re.findall("[+]", txt1)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# функція findall() повертає список з усіма збігами
x = re.findall("ai", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# якщо збігів немає повертається порожній список
x = re.findall("Portugal", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# search() шукає збіг у рядку та повертає об'єкт Match, якщо збіг є
# якщо є більше одного збігу, буде повернено лише перший збіг
x = re.search("\s", txt)
print(txt)
print("The first white-space character is locates in position:", x.start())
# якщо збігів не знайдено повертається значення None
x = re.search("Portugal", txt)
print(x)
# функція split() повертає список, де рядок був розділений при кожному збігу
x = re.split("\s", txt)
print(x)
# можна контролювати кількість входжень вказавши maxsplit параметр
x = re.split("\s",txt,1)
print(x)
# sub() замінює збіги текстом за вашим вибором
x = re.sub("\s", "_", txt)
print(x)
# можна контролювати кількість замін вказавши count параметр
x = re.sub("\s", "_", txt, 1)
print(x)
# об'єкт відповідності - містить інформацію про пошук та результат
# span() - повертає кортеж, що містить початкову та кінцеву позиції збігу
# string - повертає рядок, переданий у функцію
# group() - повертає частину рядка, де був збіг
x = re.search("ai", txt)
print(x)
# вивести позицію (початкову та кінцеву позиції) першого збігу
# регулярний вираз шукає будь-які слова, які починаються з верхнього регістру "S":
x = re.search(r"\bS\w+", txt)
print(x.span())
# вивести рядок, переданий у функцію
print(x.string)
# вивести частину рядка, де був збіг
print(x.group())

