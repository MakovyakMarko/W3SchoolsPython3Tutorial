# набір це колекція, яка є невпорядкованою, незмінною та неіндексованою
set0 = {"apple", "banana", "cherry"}
print(set0)
set1 = {"apple", "apple"}
print(set1)
# значення 1 і True вважаються однаковими значеннями в set-ах
set2 = {"apple", 1, True, 2}
print(set2)
# щоб визначити кількість елементів в set використовується функція len
print(len(set0),",", len(set2))
# елементи набору (set-у) можуть мати будь-який тип даних
set3 = {1,2,3,6,5}
set4 = {"apple", "banana"}
set5 = {True, False, False}
print(set3)
print(set4)
print(set5)
# набір може містити дані різних типів
set6 = {"apple", 32, "male", True}
print(set6)
print(type(set6))
# constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)
