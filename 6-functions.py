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
