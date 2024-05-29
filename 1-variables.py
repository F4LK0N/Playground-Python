print("### VARIABLES ###")
x = 1
print(x)
print(type(x))

y = "Text"
print(y)
print(type(y))


print("## Many Values to Multiple Variables ##")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


print("## One Value to Multiple Variables ##")
x = y = z = "Orange"
print(x)
print(y)
print(z)


print("## Unpack a Collection ##")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


print("## Output - Comma ##")
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


print("## Output - Concat ##")
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


print("## Output - Sum ##")
x = 5
y = 10
print(x + y)


print("## Global ##")
xG1 = "awesome"
def fXG1():
    xG1 = "fantastic"
    print("Python is " + xG1)
fXG1()
print("Python is " + xG1)


print("## Global Keyword ##")
xG2 = "awesome"
def fXG2():
    global xG2
    xG2 = "fantastic"
fXG2()
print("Python is " + xG2)
