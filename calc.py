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

    opt = input('Option: ').strip().upper()
    while opt not in '123456789':
        opt = input('Option:').strip().upper()

    if opt == '9':
        break


    


