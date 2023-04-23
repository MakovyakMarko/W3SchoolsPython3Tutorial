# "a" - append додає до кінця файлу
f = open("demofile2.txt", "a")
f.write("Now the file has more content!\n")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
f.close()
# "w" - write - перезаписує файл
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt", "r")
print(f.read())
f.close()
# створіть файл demofile_x
import os
f = open("demofile_x.txt", "x")
f.close()

# створіть файл demofile_w, якщо він не існує
f = open("demofile_w.txt", "w")
f.close()
