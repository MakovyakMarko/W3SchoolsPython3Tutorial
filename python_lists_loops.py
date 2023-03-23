thislist = ["apple", "banana", "cherry"]
# прокрутка списку за допомогою циклу
for x in thislist:
    print(x)
# прокрутка посилаючись на індексний номер
for i in range(len(thislist)):
    print(thislist[i])
# прокрутка за допомогою while циклу
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
# list comprehension це найкротший синтаксис для циклічного перегляду списків
[print(x) for x in thislist]