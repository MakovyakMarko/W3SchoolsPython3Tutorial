f = open("demofile.txt","r")
#print(f.read())
# може знадобитись вказати шлях до файлу, якщо в нього інше роташування
# f = open("D:\\myfiles\welcome.txt","r")
# print(f.read)
# можна вказати, скільки символів ви хочете повернути
#print(f.read(5))
# можна повернути рядок за допомогою readline() методу
#print(f.readline())
# можна прочитати два рядки, треба добавити ще один readline()
#print(f.readline())
# переглядаючи рядки файлу, ви можете прочитати весь файл, рядок за рядком
for x in f:
    print(x)
# рекомендується закривати файл, коли робота з ним закінчена
f.close()

# у деяких випадках, через буферизацію зміни, внесені у файл, можуть
# не відображатись, доки ви не закриєте файл
