fruits = ["apple", "banana", "cherry"]
# for використовується виконання набору опареторів
# один раз для кожного елемента в послідовності
for x in fruits:
    print(x)
# for в рядку
for x in "banana":
    print(x)
# зупинити цикл до того, як він пройде через усі елементи
for x in fruits:
    print(x)
    if x == "banana":
        break
# перервати перед друком
for x in fruits:
    if x == "banana":
        break
    print(x)
# за допомогою оператора continue ми можемо зупинити поточну
# ітерацію і продовжити наступну
for x in fruits:
    if x == "banana":
        continue
    print(x)
# щоб прокрутити набір коду задану кількість разів, ми можемо використати
# функцію range()
for x in range(6):
    print(x)
# можна вказати початкове значення вказавши параметр
for x in range(1,6):
    print(x)
# можна вказати на скільки зібльшувати ітерацію, додавши третій параметр
for x in range(0, 30, 3):
    print(x)
# else оператор в циклі for визначає блок коду, який буде виконано після
# завершення циклу
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# блок else не буде виконано, якщо цикл зупинено оператором break
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")
# вкладений цикл буде виконуватись один раз для кожної ітерації "зовнішнього циклу"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
# якщо for цикл порожній вставте pass щоб уникнути помилки
for x in [0,1,2]:
    pass
