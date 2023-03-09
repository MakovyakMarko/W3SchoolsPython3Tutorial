x = 1 #int
y = 2.8 #float
z = 1j #complex
print(type(x))
print(type(y))
print(type(z))

x1 = 1
y1 = 2345684857895765
z1 = -243563
print(type(x1))
print(type(y1))
print(type(z1))

x2 = 1.10
y2 = 1.0
z2 = -35.59
print(type(x2))
print(type(y2))
print(type(z2))

x3 = 35e3
y3 = 12E4
z3 = -87.7e100
print(x3)
print(y3)
print(z3)
print(type(x3))
print(type(y3))
print(type(z3))

x4 = 3+5j
y4 = 5j
z4 = -5j
print(x4)
print(y4)
print(z4)
print(type(x4))
print(type(y4))
print(type(z4))

x5 = 1
y5 = 2.8
z5 = 1j
#convert from int to float
a = float(x5)
#convert from float to int
b = int(y5)
#convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
#не можна перетворити комплексне число на інший тип чисел

import random
print(random.randrange(1,10))