try:
    print(x)
except:
    print("An exception occurred")
# можна визначити скільки завгодно блоків винятків
try:
    print(x)
except NameError:
    print("Variable is not defined")
except:
    print("Something else went wrong")
# else буде виконано, якщо не було викликано жодних помилок
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
# finally буде виконано незалежно від того, викликає помилку блок try чи ні
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
# finally може бути корисним для закриття файлів і очищення ресурсів
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close() # програма продовжує працювати не залишаючи файл відкритим
except:
    print("Something went wrong when opening the file")
# щоб створити виняток використовуйте ключове слово raise. Можна визначити
# який тип помилки викликати, і текст, який потрібно надрукувати користувачеві
x = -1
if x<0:
    pass
    #raise Exception("Sorry, no numbers below zero")

x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")