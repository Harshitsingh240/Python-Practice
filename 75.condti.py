# Write a calculator program using if-elif-else.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter + or - : ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
else:
    print("Invalid operator")

