#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This is the implementatiom of a simple postfix notation (polish) calculator.
    It's for fun... for learn to use Vi... to use Git and GitHub a little!
'''


print('=-'*30)
print('>>> SIMPLE POLISH NOTATION CALCULATOR <<<')
print('=-'*30)

while True:
    print('>>> MENU <<<')
    print('''
        1. Type number
        2. Stack up
        3. Add
        4. Subtract
        5. Multiply
        6. Divide
        7. Unstack
        8. Clear
        9. Quit
    ''')

    a = 0             # accumulator
    x = 0             # number
    stacked = False   # no value stacked up

    opt = input('Option: ').strip().upper()
    while opt not in '123456789':
        opt = input('Option:').strip().upper()

    if opt == '1':
        x = float(input('x = '))
        print('-'*30)
        print('Value inserted!')
        print('-'*30)

    if opt == '2':
        if stacked == True:
            print('A value is already stacked!')
        else:
            a = x
            print('-'*30)
            print('Value stacked')
            print('-'*30)

    if opt == '3':
        if stacked == False:
            print('Stack up a value first@')
        else:
            a += x
            print('-'*30)
            print(f'Addiction: result {a}')
            print('-'*30)

    if opt == '4':
        if stacked == False:
            print('Stack up a value first@')
        else:
            a -= x
            print('-'*30)
            print(f'Subtraction: result {a}')
            print('-'*30)
        
    if opt == '5':
        if stacked == False:
            print('Stack up a value first@')
        else:
            a *= x
            print('-'*30)
            print(f'Multiplying: resilt {x}')
            print('-'*30)

    if opt == '6':
        if stacked == False:
            print('Stack up a value first@')
        else:
            a /= x
            print('-'*30)
            print(f'Division: result {x}')

    if opt == '7':
        if stacked == False:
            print('Stack up a value first@')
        else:
            x = a
            print('-'*30)
            print('Value unstacked')
            print('-'*30)

    if opt == '8':
        a = x = 0
        print('Cleaned: a = 0 and x = 0')

    if opt == '9':
        break

print('=-'*30)
print('Thank you for use our calculator!')
print('=-'*30)

