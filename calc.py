#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This is the implementatiom of a simple postfix notation (polish) calculator.
    It's for fun... for learn to use Vi... to use Git and GitHub a little!
'''


print('=-'*30)
print('>>> SIMPLE POLISH NOTATION CALCULATOR <<<')
print('=-'*30)

a = x = 0          # initalize stack and value
stacked = False    # initialize stack flag

while True:
    print('[T]ype number | Stac[K] up | [A]dd | [S]ubtract | [M]ultiply | [D]ivide | [U]nstack | [C]lear | [Q]uit')

    opt = input('Option: ').strip().upper()
    while opt not in 'TKASMDUCQ':
        opt = input('Option:').strip().upper()

    if opt == 'T':
        x = float(input('x = '))
        print('-'*30)
        print('Value inserted!')
        print('-'*30)

    if opt == 'K':
        print(f'stacked = {stacked}')
        if stacked == True:
            print('A value is already stacked!')
        else:
            a = x
            stacked = True
            print(f'stacked = {stacked}')
            print('-'*30)
            print('Value stacked')
            print('-'*30)

    if opt == 'A':
        print(f'Stacked = {stacked}')
        if stacked == False:
            print('Stack up a value first@')
        else:
            a += x
            print('-'*30)
            print(f'Addiction: result {a}')
            print('-'*30)

    if opt == 'S':
        if stacked == False:
            print('Stack up a value first@')
        else:
            a -= x
            print('-'*30)
            print(f'Subtraction: result {a}')
            print('-'*30)
        
    if opt == 'M':
        if stacked == False:
            print('Stack up a value first@')
        else:
            a *= x
            print('-'*30)
            print(f'Multiplying: resilt {x}')
            print('-'*30)

    if opt == 'D':
        if stacked == False:
            print('Stack up a value first@')
        else:
            a /= x
            print('-'*30)
            print(f'Division: result {x}')

    if opt == 'U':
        if stacked == False:
            print('Stack up a value first@')
        else:
            x = a
            print('-'*30)
            print('Value unstacked')
            print('-'*30)

    if opt == 'C':
        a = x = 0
        print('Cleaned: a = 0 and x = 0')

    if opt == 'Q':
        break

print('=-'*30)
print('Thank you for use our calculator!')
print('=-'*30)

