tuple = ("apple", "banana", "cherry")
for x in tuple:
    print(x)
# за індексом, через діапазон довжину
for i in range(len(tuple)):
    print(tuple[i])
# while
i = 0
while i < len(tuple):
    print(tuple[i])
    i += 1
