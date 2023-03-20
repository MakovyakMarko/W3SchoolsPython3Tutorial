x = 10
y = 5
# арифметичні оператори
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
# оператори присвоєння
z = 5
print(z)
z += 5
print(z)
z -= 3
print(z)
z *= 3
print(z)
z /= 3
print(z)
z %= 3
print(z)
z = 10
z //= 3
print(z)
z **= 3
print(z)
z &= 3
print(z)
z |= 3
print(z)
z ^= 3
print(z)
z = 10
z >>= 3
print(z)
z <<= 3
print(z)
# оператори порівняння
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
# логічні оператори
print(x > 5 and x >= 10)
print(x > 5 or x > 10)
print(not(x < 5 and x < 10))
# оператори ідентифікації
x1 = ["apple", "banana"]
y1 = ["apple", "banana"]
z1 = x1
print(x1 is z1)
print(x1 is y1)
print(x1 == y1)
print(x1 is not z1)
print(x1 is not y1)
print(x1 != y1)
# оператори членства
print("banana" in x1)
print("pineapple" not in x1)
# побітові оператори
print(6 & 3) # "AND" ставить в кожний біт 1, якщо обидва біти дорівнюють 1
print(6 | 3) # "OR" ставить в кожний біт 1, ящко хоча б один біт дорівнює 1
print(6 ^ 3) # "XOR" співідносить біти, і ставить в кожний біт 1, якщо тільки один з них 1 (якщо 2 = 1, або 2 = 0 то ставить 0)
print(~3) # "NOT", інвертує всі біти, змінює 0 на 1 і 1 на 0
print(3 << 2) # "zero fill left shift", вставляє вказану кількість нулів (2) справа і дозволяє відпасти такій самій кіл-ті крайніх лівих бітів
print(8 >> 2) # "zero fill right shift", вставляє вказану кількість нулів (2) зліва і дозволяє відпасти такій самій кіл-ті крайніх правих бітів
# пріорітет оператора
print((6 + 3) - (6 + 3)) # дужки майють найбільший пріорітет
print(100 + 5 * 3) # множення має вищий пріорітет ніж додавання
# приорітетність, від найвищої
print((6 + 3)* 2) # приорітет дужок
print(3* 3**3) # приорітет степеня
print(100 + ~3) # +х, -x, ~x - пріорітет NOT, інертована 3 = -4, 100 + -4 = 96
print(100 / 25 * 2 + 2) # /,*, //, %
print(2 + 2 - 3) # +,-
print(3<<2)  # <<, >>
print(6 & 3) # &
print(6 ^ 3) # ^
print(6 | 3) # |
print(x1 == y1) # ==, !=, >, >=, <, <=, is, is not, in, not in
print(not 5 == 6) # not
print(1 or 2 and 3) # and має вищий пріорітет ніж or і нам потрібно спочатку обчислити вираз and. Розрхунок вище : 1 or 3 = 1
print(4 or 5 + 10 or 8) # оператор or має нижчий пріорітет ніж додавання, тому 4 or 15 or 8 = 4
