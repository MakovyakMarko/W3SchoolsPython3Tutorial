set1 = {"apple", "banana", "cherry"}
set2 = {"microsoft", "google", "apple"}
# difference() повертає набір, який містить елементи, які існують лише в наборі 1, а не в наборі 2
set3 = set1.difference(set2)
print(set3)
# difference_update() видаляє елементи, які існують в обох наборах
set4 = {"apple", "banana", "cherry"}
set5 = {"microsoft", "google", "apple"}
set6 = set4.difference_update(set5)
print(set4)
# isdisjoint() повертає True, якщо жодного елемента з набору 1 немає в наборі 2
z = set1.isdisjoint(set2)
print(z)
# issubset() повертає True, якщо всі елементи набору х присутні в наборі у
x = {"a", "b", "c"}
y = {"a", "d", "b","e","c"}
z1 = x.issubset(y)
print(z1)
# issuperset() повертає True, якщо все елементи набору у присутні в наборі х
z2 = x.issuperset(y)
print(z2)