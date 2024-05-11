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




### ERRORS ###
print("### ERRORS ###")



### FUNCTIONS ###
print("### FUNCTIONS ###")



### CLASSES ###
print("### CLASSES ###")




