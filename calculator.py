# create a python calculator
num1 = float(input("First number: "))
operator = input("Operator: (+ , - , * , /): ")
num2 = float(input("Second number: "))
if operator == "+":
    print("Result: ", num1+num2)
elif operator == "-":
    print("Result: ", num1-num2)
elif operator == "*":
    print("Result: ", num1*num2)
elif operator == "/":
    if num2 == 0:
        print("cannot devide by zero")
    else:
        print("Result:",num1/num2)
else:
    print("invalid operator")
