'''
7.3. The assert statement
Assert statements are a convenient way to insert debugging assertions into a program:

assert_stmt ::=  "assert" expression ["," expression]
The simple form, assert expression, is equivalent to

if __debug__:
    if not expression: raise AssertionError
The extended form, assert expression1, expression2, is equivalent to

if __debug__:
    if not expression1: raise AssertionError(expression2)
These equivalences assume that __debug__ and AssertionError refer to the built-in variables with those names. In the current implementation, the built-in variable __debug__ is True under normal circumstances, False when optimization is requested (command line option -O). The current code generator emits no code for an assert statement when optimization is requested at compile time. Note that it is unnecessary to include the source code for the expression that failed in the error message; it will be displayed as part of the stack trace.

Assignments to __debug__ are illegal. The value for the built-in variable is determined when the interpreter starts.
'''

#
assert 3, 5
assert 2, 0
assert 1, 0

assert 1

# assert 0  # AssertionError
# assert 0, 0  # AssertionError: 0
# assert 0, 5    # AssertionError: 5

print(__debug__)  # True

# __debug__ = False  # SyntaxError: cannot assign to __debug__

# assert [], 'Value should not be zero or empty'

'''
AssertionError: Value should not be zero or empty
'''

assert 0, 'Value should not be zero or empty'




