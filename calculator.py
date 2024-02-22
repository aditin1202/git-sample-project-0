a=int(input("enter number 1:"))
o = input("Enter operator: ")
b =int(input("Enter number 2: "))

   
if o[0] in ['+', '-', '*', '/']:
    if o[0] == '+':
        out = a + b

    elif o[0] == '*':
        out = a * b
    elif o[0] == '/':
        out = a//b
        if b == 0:
            print("Error: Division by zero is not allowed.")
            exit()
        out = a / b
    print("Output: ", out)
else:
    print("Error: Invalid Operator")
