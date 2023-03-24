# для об'єднання наборів використовують методи union() i update()
set1 = {"a", "b", "c"}
set2 = {1,3,2}
# union() повертає новий набір, що містить елементи обох наборів
set3 = set1.union(set2)
print(set3)
# update() вставляє елементи з одного набору в інший
set1.update(set2)
print(set1)
# метод intersection_update() збереже лише елементи, які присутні в обох наборах
x = {"apple", "banana", "cherry"}
y = {"microsoft", "google", "apple"}
x.intersection_update(y)
print(x)
# метод intersection() поверне новий набір, який містить лише елементи,
# присутні в обох наборах
x1 = {"apple", "banana", "cherry"}
y1 = {"microsoft", "google", "apple"}
z = x.intersection(y)
print(z)
# щоб зберегти всі елементи, але не дублікати, використовуйте symmetric_difference_update()
x2 = {"apple", "banana", "cherry"}
y2 = {"microsoft", "google", "apple"}
x2.symmetric_difference_update(y2)
print(x2)
# метод symmetric_difference() поверне новий набір, який містить лише елементи,
# які НЕ присутні в обох наборах (тобто без дублючихся)
x3 = {"apple", "banana", "cherry"}
y3 = {"microsoft", "google", "apple"}
z1 = x3.symmetric_difference(y3)
print(z1)
# примітка. Значення 1 і True в наборах розглядаються як дублікати
x4 = {"apple", "banana", 1}
y4 = {"microsoft", "google", True}
z2 = x4.symmetric_difference(y4)
print(z2)