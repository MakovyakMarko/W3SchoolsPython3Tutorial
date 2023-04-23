# PIP - це менеджер пакетів для пакетів Python або модулів. Пакет
# містить усі файли, необхідні для модуля. Модулі - це бібліотеки
# коду Python, які можна включити у свій проект.
# імпорутйте та використовуйте "camelcase"
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
