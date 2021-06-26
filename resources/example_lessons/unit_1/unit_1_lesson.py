# Welcome to PDX Code Guild!
# single-line comments use pound signs #
# everything to the right of the pound sign will be a comment

'''
Multi-line
comment with
single quotes
'''

"""
Multi-line 
comment with
double quotes
"""

'''
Comments

- organize code
- explain code
- exclude lines of code for testing
'''

# ------------------------------------------------------------------------------- #

# a "function" is a named piece of code that performs a specific task
# Python comes with many built-in functions
# functions must be executed using parentheses after their name ()

# print(data) - a built-in function to display the 'data' in the terminal

# express an opinion about spam
# print("I don't like spam!") # I don't like spam!

# --------------------------------------------------------------------------------------- #

# Datatype: string (str)

# strings are sequences of textual characters surrounded by quotes

'cat'
"dog"
'01237461123'
"3.141592654"
'' # blank string
"" # blank string

# -------------------------------------------------------------------------------------- #

# concatenation - adding strings together to form a single string

# print('pdx' + 'code') # pdxcode

# print three words with space between
# print('pdx' + ' ' + 'code' + ' ' + 'guild') # pdx code guild

# build a word one letter at a time
# print('c' + 'a' + 't') # cat

# print('4' + '4') # 44 - both 4s are strings
# print(4 + 4) # 8 - both 4s are integers
# print('4' + 4) # TypeError: can only concatenate str (not "int") to str

# ---------------------------------------------------------------------------------- #

# a "method" is a function (needs parentheses to be executed)
# methods only manipulate the object to which they belong

# an object's methods are accessed using a dot after the object

# .upper() - return an uppercase version of the string
# print('abcd'.upper()) # ABCD
# print('wxyz'.upper()) # WXYZ

# .title() - return a lowercased string with the first letter of each word capitalized
# print('pOrTlAnD, oReGoN'.title()) # Portland, Oregon

# ------------------------------------------------------------------------------------- #

# OOPS! Forgot parentheses on the method call
# print('wxyz'.upper) # <built-in method upper of str object at 0x000002571CCE7770>

# -------------------------------------------------------------------------------------- #

# Escape Characters

# denoted with a backslash \ before the character
# allow characters to be placed within a string that would normally cause errors
# allow formatting of strings
# other uses...

# Python uses quotation marks to begin and end strings
# "Hello "world"" # Error! Double quotes cancel each other
# 'Hello 'world''  # Error! Single quotes cancel each other

# Solution 1: mismatmached sets of quotes
# print('hello "world"') # hello "world"
# print("hello 'world'") # hello 'world'

# Solution 2: escape characters
# print("Hello \"world\"") # Hello "world" - \" escape character
# print('Hello \'world\'') # Hello 'world' - \' escape characters

# escape characters can also format strings
# print("A\nB\nC") # \n - new line character
# print("A\tB\tC") # \t - horizontal tab character