x = "awesome"
def  myfunc():
    print("Python is " + x)

myfunc()

x1 = "awesome"
def myfunc1():
    x1 = "fantastic"
    print("Python is " + x1)
myfunc1()

print("Python is " + x1)

def myfunc2():
    global x3
    x3 = "fantastic"

myfunc2()
print("Python is " + x3)

x4 = "awesome"
def myfunc3():
    global x4
    x4 = "fantastic"
myfunc3()
print("Python is " +x4)