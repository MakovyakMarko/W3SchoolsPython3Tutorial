# іноді є частини тексту, які ви не контролюєте, можливо вони походять
# із бази даних або введені користувачем.
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
# можна додати параметри у фігурні дужки, щоб указати, як конвертувати
# значення. Відформатуйте ціну, яка має відображатись як число з двома
# десятковими знаками
txt = "The price is {:.2f} dollars"
print(txt.format(price))
# форматування рядка
# добавити відступ в рядок, "<" для встановлення зліва від відступу
txt = "We have {:<8} chickens."
print(txt.format(49))
# "<" для встанолення справа від відступу
txt = "We have {:>8} chickens."
print(txt.format(49))
# "^" для встановлення по центру від відступів
txt = "We have {:^8} chickens."
print(txt.format(49))
# "=" для встановлення мінусу або плюсу на саму ліву позицію
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
# "+" для того щоб завжди вказувати додатнє чи від'ємне число
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3,7))
# "-" для того щоб завжди вказувати від'ємні числа(додатні числа
# відображаються без знаку)
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3,7))
# " " (пробіл) для додавання пробилу перед додатніми числами і мінусу
# перед від'ємними.
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3,7))
# "," для додавання розділителя тисяч
txt = "The universe is {:,} years old."
print(txt.format(13800000000))
# "_" для додавання _ як розділителя тисяч
txt = "The universe is {:_} years old."
print(txt.format(13800000000))
# використовуйте "b" для конвертації числа в формат бінарної системи
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
# "с" конвертує значення в unicode
txt = "The unicode version of {0} is {0:c}"
print(txt.format(234))
# "d" форматує значення в десяткову систему числення
txt = "We have {:d} chickens."
print(txt.format(0b101))
# "е" щоб перетворити число в науковий числовий формат (з малим
# регістром е)
txt = "We have {:e} chickens."
print(txt.format(5))
# "E" щоб перетворити число в науковий числовий формат (з великим
# регістром E)
txt = "We have {:E} chickens."
print(txt.format(5))
# використовуйте "f" щоб перетворити число на число з фіксованою комою,
# за замовчуванням із 6 десятковими комами, але використовуйте крапку,
# після якої йде число, щоб указати кількість десяткових знаків
txt = "The price is {:.2f} dollars."
print(txt.format(45))
txt = "The price is {:f} dollars."
print(txt.format(45))
# використовйте "F" щоб перетворити число на число з фіксованою комою,
# але відображайте nf i nan як INF i NAN
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
txt = "The price is {:f} dollars."
print(txt.format(x))
# "g" основний формат
txt = "We have {:g} chickens."
print(txt.format(0b101))
# "G" основний формат (використовуючи Е
# великого регістру для наукових заміток)
txt = "We have {:G} chickens."
print(txt.format(5))
# "о" для конвертації в вісімкову систему числення
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))
# "x" для конвертації в шістнадцяткову систему числення
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))
# "X" для конвертації в шістнадцяткову систему числення в великому регістрі
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))
# "n" цифоровий формат
txt = "The octal version of {0} is {0:n}"
print(txt.format(0b101))
# "%" для конвертації числа в проценти
txt = "You scored {:%}"
print(txt.format(0.25))
txt = "You scored {:.0%}"
print(txt.format(0.25))

# якщо ви хочете використовувати більше значень, просто
# додайте більше значень до методу format()
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity,itemno,price))
# можна використовувати номери індексів, щоб переконатися, що значення
# в правильних заповнювачах
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity,itemno,price))
# крім того, можна посилатись на те саме значення більше одного разу,
# викорстовуйте для цього номер індексу
age = 32
name = "Makro"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
# можна використовувати іменовані індекси, ввівши назву у фігурних
# дужках, але тоді ви повинні використовувати імена, коли передаєте
# значення параметрів
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))