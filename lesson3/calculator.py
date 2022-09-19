a = float(input("select first number:"))
b = float(input("select second number:"))
op = input("выберете действие:")

if op == "+":
    print(a + b)


if op == "-":
    print(a - b)

if op == "*":
    print(a * b)

if op == "/" and b != 0:
    print(a / b)