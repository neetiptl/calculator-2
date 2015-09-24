"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator_2():
    calculate_this = raw_input("Give us an expression to evaluate: ")
    while calculate_this!= ('q' or 'Q'):
        tokens = calculate_this.split(' ')
        operator = tokens[0]
        num1 = float(tokens[1])
        if len(tokens) > 2 :
            num2 = float(tokens[2])
        if operator == '+':
            answer = add(num1,num2) 
        if operator == '-':
            answer = subtract(num1, num2)
        if operator == '*':
            answer = multiply(num1, num2)
        if operator == '/':
            answer = divide(num1, num2)
        if operator == 'square': 
            answer = square(num1)
        if operator == 'cube':
            answer = cube(num1)
        if operator == 'pow':
            if num2 < 0:
                num1 = 1/num1
                num2 = abs(num2)
            answer = power(num1, num2)
        if operator == 'mod':
            answer = moded(num1, num2)
        print answer
        calculate_this = raw_input("Give us an expression to evaluate: ")

calculator_2()