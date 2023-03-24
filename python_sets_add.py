thisset = {"apple", "banana", "cherry"}
# додати елемент можна через метод add
thisset.add("orange")
print(thisset)
# щоб додати елементи з іншого набору використовуйте матод update()
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# метод update() може додати буль-який ітерований об'єкт - списки, кортежі, словники
mylist = ["kiwi", "blackcurrant"]
thisset.update(mylist)
print(thisset)
