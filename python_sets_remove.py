thisset = {"apple", "banana", "cherry"}
# якщо елемента вказаного в remove() не існує - виникне помилка
thisset.remove("apple")
print(thisset)
# якщо елемента вказаного в discard() не існує - помилка НЕ виникне
thisset.discard("banana")
print(thisset)
# можна використовувати метод pop(), але він видалить випадковий елемент
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# clear() очищає набір
thisset.clear()
print(thisset)
# del повністю видалить набір
del thisset
print(thisset)
