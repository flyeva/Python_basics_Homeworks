x = float(input("Enter first number "))
operation = input("Operation ")
y = float(input("Enter second number "))

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("I dont't recognize the operation.")
