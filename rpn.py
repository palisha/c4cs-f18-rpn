#!/usr/bin/env python3

import operator
import readline
#import colors
from termcolor import colored
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '<': operator.lt
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
            #print (colored(stack,'green'))
        except ValueError:
            function = operators[token]
           # if(token == '<'):
            #    print(token)
            #print(colored(token,'green'))
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
       # print (colored(stack,'red'))
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
