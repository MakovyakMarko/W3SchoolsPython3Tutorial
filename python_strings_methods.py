
x = "Hello World"
print(x.capitalize())
print(x.casefold())
print(x.center(20))
print(x.count("l"))
x1 = "My name is Ståle"
print(x1.encode())
print(x.endswith("d"))
x2 = "H\te\tl\tl\to"
print(x2.expandtabs(2))
print(x.find("Wo"))
x3 = "For only {price:.2f} dollars!"
print(x3.format(price = 49))
print(x.index("Wo"))
x4 = "Company12"
print(x4.isalnum())
x5 = "CompanyX"
print(x5.isalpha())
x6 = "\u0033"
print(x6.isdecimal())
x7 = "5080"
print(x7.isdigit())
x8 = "Demo"
print(x8.isidentifier())
x9 = "hello world"
print(x9.islower())
x10 = "34234"
print(x10.isnumeric())
x11 = "Hello! Are you #1?"
print(x11.isprintable())
x12 = "    "
print(x12.isspace())
x13 = "Hello! And Welcome To My World!"
print(x13.istitle())
x14 = "THIS IS NOW!"
print(x14.isupper())
# join all items in a tuple into a string,
# using a hash character as saparator:
myTuple = ("John", "Peter", "Vicky")
x15 = "#".join(myTuple)
print(x15)
x16 = "banana"
print(x16.ljust(20), "is my favorite fruit.")
x17 = "Hello my FRIENDS"
print(x17.lower())
x18 ="  banana  "
print("of all fruits", x18.lstrip(), "is my favorite")
x19 = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(x19.translate(mytable))
x20 = "I could eat bananas all day"
print(x20.partition("bananas"))
x21 = "I like bananas"
print(x21.replace("bananas", "apples"))
x22 = "Mi casa, su casa."
print(x22.rfind("casa"))
print(x22.rindex("casa"))
x23 = "banana"
print(x23.rjust(20), "is my favorite fruit.")
x24 = "I could eat bananas all day, bananas are my favorite fruit"
print(x24.rpartition("bananas"))
x25 = "apple, banana, cherry"
print(x25.rsplit(", "))
x26 = "  banana  "
print("of all fuits" ,x26.rstrip(), "is my favorite")
x27 = "welcome to the jungle"
print(x27.split())
x28 = "Thank you for the music\nWelcome to the jungle"
print(x28.splitlines())
x29 = "Hello, welcome to my world."
print(x29.startswith("Hello"))
x30 = "    banana    "
print("of all fruits",x30.strip(), "is my favorite")
x31 = "Hello, My Name Is PETER"
print(x31.swapcase())
x32 = "Welcome to my world"
print(x32.title())
mydict = {83: 80}
x33= "Hello Super Sam!"
print(x33.translate(mydict))
print(x.upper())
x34 = "50"
print(x34.zfill(10))