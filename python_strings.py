print("Hello")
print('Hello')

a = "Hello"
print(a)

a1 = """Отче наш, що єси на Небесах,
Нехай святиться Ім'я Твоє,
Нехай прийде Царство Твоє,
Нехай буде Воля Твоя, як на Небі так і на Землі,
Хліб наш насущний, дай нам сьогодні,
І прости нам провини наші, як і ми прощаєм винуватьцям нашим,
І не веди нас у спокусу, але визволи нас від лукавого."""
print(a1)

a2 = '''Отче наш, що єси на Небесах,
Нехай святиться Ім'я Твоє,
Нехай прийде Царство Твоє,
Нехай буде Воля Твоя, як на Небі так і на Землі,
Хліб наш насущний, дай нам сьогодні,
І прости нам провини наші, як і ми прощаєм винуватьцям нашим,
І не веди нас у спокусу, але визволи нас від лукавого.'''
print(a2)
#рядок це масив, що починається з 0, 1 = е
a3= "Hello, World"
print(a3[1])
#за допомогою for ми прокручуємо рядок, який є масивом
for x in "banana":
    print(x)

a4 = "Hello, World"
print(len(a4))

txt ="The best thing in life are free!"
print("free" in txt)

txt ="The best thing in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt ="The best thing in life are free!"
print("expensive" not in txt)

txt ="The best thing in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")


