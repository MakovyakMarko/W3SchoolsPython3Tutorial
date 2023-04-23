# щоб видалити файл потрібно імпортувати модуль ОС і запуститиу його
# os.remove() фуекцію
import os
#os.remove("demofile_x.txt")
# щоб уникнути помилки, ви можете перевірити, чи файл існує, перш
# ніж спробувати його видалити:
if os.path.exists("demofile_w.txt"):
    os.remove("demofile_w.txt")
else:
    print("The filee does not exist")
# можна видаляти папки, але лише порожні
os.rmdir("myfolder")