"""
    This module contains code from
    Think Python by Allen B. Downey
    http://thinkpython.com

    Copyright 2012 Allen B. Downey
    License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
    
    This is to test out a few basic functions in Python from Chapter 3 of Think Python 2

    Note: Although this is saved in a .py file, code was run on an interpreter to get results
"""

"""
    Write a function named right_justify that takes a string named s as a parameter and prints 
    the string with enough leading spaces so that the last letter of the string is in column 70
    of the display.
    
    >>> right_justify('monty')
"""
>>> def right_justify(str):
...     position = 70 - len(str)
...     print(str.rjust(position))

>>> right_justify('Monty')
#                                                            Monty

"""
    A function object is a value you can assign to a variable or pass as an argument. For example,
    do_twice is a function that takes a function object as an argument and calls it twice:

    def do_twice(f):
        f()
        f()

    Here’s an example that uses do_twice to call a function named print_spam twice.
    
    def print_spam():
        print('spam')

    do_twice(print_spam)

    1. Type this example into a script and test it.
    2. Modify do_twice so that it takes two arguments, a function object and a value, and calls
        the function twice, passing the value as an argument.
    3. Copy the definition of print_twice from earlier in this chapter to your script.
    4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
    5. Define a new function called do_four that takes a function object and a value and calls the
        function four times, passing the value as a parameter. There should be only two statements
        in the body of this function, not four.
"""
# 1.
>>> def do_twice(f):
...     f()
...     f()
...
>>> def print_spam():
...     print("spam")
...
>>> do_twice(print_spam)
# spam
# spam

# 2.
>>> def do_twice(func, val):
...     func(val)
...     func(val)
...
>>> def print_something(val):
...     print(val)
...
>>> do_twice(print_something, "Eric the half a bee.")
# Eric the half a bee.
# Eric the half a bee.

# 3. and 4.
>>> def print_twice(bruce):
...     print(bruce)
...     print(bruce)
...
>>> print_twice("Spam, lovely spam.")
# Spam, lovely spam.
# Spam, lovely spam.
>>> print_twice(42)
# 42
# 42
>>> import math
>>> print_twice(math.pi)
# 3.141592653589793
# 3.141592653589793

# 5. (Assuming the predefined do_twice function is still active)
>>> def do_twice(func, val):
...     func(val)
...     func(val)
...
>>> def do_four(func, val):
...     do_twice(func, val)
...     do_twice(func, val)
...
>>> do_four(print, "Spam!")
# Spam!
# Spam!
# Spam!
# Spam!