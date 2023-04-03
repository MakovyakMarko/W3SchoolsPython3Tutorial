# імпортуємо модуль з файлу pyton_modules_mymodule
import python_modules_mymodule
# викликаємо функцію з модуля
pyton_modules_mymodule.greating("Marko")

x = python_modules_mymodule.person1["age"]
print(x)

import python_modules_mymodule as module
a = module.person1["name"]
print(a)

import platform
x1 = platform.system()
print(x1)
x2 = dir(platform)
print(x2)
x3 = platform.architecture()
print(x3)

from python_modules_mymodule import person1
print(person1["country"])
