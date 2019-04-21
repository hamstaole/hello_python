num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num2 + num1)
elif op == "-":
    print(num2 - num1)
elif op == "/":
    print(num2 / num1)
elif op == "*":
    print(num2 * num1)
else:
    print("Invalid Operator. ")
