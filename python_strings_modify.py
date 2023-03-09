a = "Hello, World!"
# перевести у верхній регістр
print(a.upper())
# перевести у нижній регістр
print(a.lower())
#видаленні пробілів strip
b = " Hello, World! "
print(b)
print(b.strip())
# замінити частину рядка, вказуєм що замінити
# і на що замінити через кому
c = "Hello, World!"
print(c.replace("World", "Marko"))
# розділити рядок, повертає список, де текст
# між вказаним роздільником стає елементом списку.
d = "Hello, World!"
print(d.split(","))
print(d.split("l"))