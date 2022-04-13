from unittest import case


operator = 'start'

while operator: 
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))
    operator = input("opertator ex) +, -, *, /, //, **, q: ")
    res = 0
    if operator == 'q':
        operator = None
    elif operator == '+':
        res = num1 + num2
    elif operator == '-':
        res = num1 - num2
    elif operator == '*':
        res = num1 * num2
    elif operator == '/':
        res = num1 / num2
    print(res)