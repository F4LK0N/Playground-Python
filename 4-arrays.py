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
