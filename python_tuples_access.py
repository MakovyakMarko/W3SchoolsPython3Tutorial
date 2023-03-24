# доступ до елемента через індекс
tuple1 = ("apple", "banana", "cherry")
print(tuple1[1])
# з кінця негативна індексація, починається з -1
print(tuple1[-1])
# діапазон індексів виводить всі значення в діапазоні, останній індекс не включено
tuple2 = ("apple", "banana", "cherry", "apple", "banana", "cherry")
print(tuple2[2:5])
# до 3 вкючно
print(tuple2[:4])
# з 2 включно
print(tuple2[2:])
# з кінця, діапазон негативних індексів
print(tuple2[-4:-1])
# перевірте, чи існує елемент
if "banana" in tuple2:
    print("Yes, 'banana' is in the fruits tuple")
if "mango" in tuple2:
    print("Yes, 'mango' is in the fruits tuple")
else:
    print("No, 'mango' is not in the fruits tuple")