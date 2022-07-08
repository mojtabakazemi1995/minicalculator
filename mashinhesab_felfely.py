# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 18:09:42 2021

@author: Mojtaba
"""


'''Mashin hesab felfely'''
import operator
num1 = input('Please enter Number1: ')
opr = input('Please enter a operator(+ - * /): ')
num2 = input('Please enter Number2: ')
oprs={'+': operator.add, '-': operator.sub,
      '*': operator.mul, '/': operator.truediv }
def isfloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
if isfloat(num1) is False or isfloat(num2) is False:
    print('Something went wrong! ')
elif len(opr) != 1 and set(opr).intersection({'+', '-', '*', '/'}) is False:
    print('The operator is not valid! ')
else:
    #print(num1 oprs[opr] num2)
    print(oprs[opr](num1,num2))
    
    