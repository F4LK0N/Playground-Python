### OUTPUTS ###
print("### OUTPUTS ###")
print("Hello World")



### VARIABLES ###
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



### CASTING ###
print("### CASTING ###")
x = str(3)
print(x)
print(type(x))

y = int(3)
print(y)
print(type(y))

z = float(3)
print(z)
print(type(z))



### STRINGS ###
print("### STRINGS ###")
print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


print("## Arrays ##")
a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)

a = "Hello, World!"
print(len(a))


print("## Check ##")
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)


print("## Slicing ##")
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])


print("## Modify ##")
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))


print("## Concatenation ##")
a = "Hello"
b = "World"
c = a + " " + b
print(c)


print("## Format ##")
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)


print("## Escape ##")
txt = "We are the so-called \"Vikings\" from the north."
print(txt)



### ARRAYS ###
print("### ARRAYS ###")
cars = ["Ford", "Volvo", "BMW"]
print(cars[0])
print(len(cars))
for x in cars:
    print(x)

cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
for x in cars:
    print(x)

cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
for x in cars:
    print(x)

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
for x in cars:
    print(x)



### CONDITIONALS ###
print("### CONDITIONALS ###")

print("## IF ##")
a = 33
b = 200
if b > a:
    print("b is greater than a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 2
print("A") if a > b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

a = 33
b = 200
if b > a:
    pass


print("## WHILE ##")
i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


print("## FOR ##")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

for x in [0, 1, 2]:
    pass



### FUNCTIONS ###
print("### FUNCTIONS ###")

def f1():
    print("Hello from a function")
f1()

def f2(fname):
    print(fname + " Refsnes")
f2("Emil")
f2("Tobias")
f2("Linus")

def f3(fname, lname):
    print(fname + " " + lname)
f3("Emil", "Refsnes")

def f4(*kids):
    print("The youngest child is " + kids[2])
f4("Emil", "Tobias", "Linus")

def f5(child3, child2, child1):
    print("The youngest child is " + child3)
f5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def f6(**kid):
    print("His last name is " + kid["lname"])
f6(fname = "Tobias", lname = "Refsnes")

def f7(country = "Norway"):
    print("I am from " + country)
f7("Sweden")
f7("India")
f7()
f7("Brazil")

def f8(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
f8(fruits)

def f9(x):
    return 5 * x
print(f9(3))
print(f9(5))
print(f9(9))

def f10():
    pass


print("## Positional Only ##")
def f11(x, /):
    print(x)
f11(3)


print("## Keyword Only ##")
def f12(*, x):
    print(x)
f12(x = 3)


print("## Positional Only and Keyword Only ##")
def f13(a, b, /, *, c, d):
    print(a + b + c + d)
f13(5, 6, c = 7, d = 8)


print("## Recursion ##")
def f14(k):
  if(k > 0):
    result = k + f14(k - 1)
    print(result)
  else:
    result = 0
  return result
f14(6)



### ERRORS ###
print("### ERRORS ###")






### CLASSES ###
print("### CLASSES ###")




