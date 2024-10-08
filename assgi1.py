# -*- coding: utf-8 -*-
"""assgi1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EzwrxxLS3_Tx_ZWuYv_AjQlefAh4KTmA

Q1. Create one variable containing following type of data:
(i) string
(ii) list
(iii) float
(iv) tuple
"""

my_variable = (
    "This is a string",   # string
    [1, 2, 3, 4],         # list
    3.14,                 # float
    (5, 6, 7)             # tuple
)
print("String:", my_variable[0])
print("List:", my_variable[1])
print("Float:", my_variable[2])
print("Tuple:", my_variable[3])

"""Q2. Given are some following variables containing data:
(i) var1 = ‘ ‘
(ii) var2 = ‘[ DS , ML , Python]’
(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
(iv) var4 = 1.
"""

var1 = ' '
var2 = '[ DS , ML , Python]'
var3 = [ 'DS', 'ML', 'Python' ]
var4 = 1.

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

"""Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) **
"""

a = 10
b = 3
result = a / b
print(result)

result = a % b
print(result)

result = a // b
print(result)

result = a ** b
print(result)

"""4 . Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type.
"""

my_list = [25, "Hello", 3.14, True, None, [1, 2, 3], (4, 5, 6), {'key': 'value'}, {9, 8, 7}, b'bytes']


for element in my_list:
    print(f"Element: {element} | Type: {type(element)}")

"""Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.
"""

A = 64
B = 2
count = 0
while A % B == 0:
    A = A // B
    count += 1

if count > 0:
    print(f"Number A can be divided by number B {count} times.")
else:
    print("Number A is not divisible by number B.")

"""Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not.

"""

int_list = list(range(1, 26))
for i in int_list:
    if i % 3 == 0:
        print(f"{i} is divisible by 3.")
    else:
        print(f"{i} is not divisible by 3.")

"""Q7. What do you understand about mutable and immutable data types? Give examples for both showing
this property.
"""

my_list = [1, 2, 3]
print("Original list:", my_list)

my_list[0] = 99
print("Modified list:", my_list)

my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)

try:
    my_tuple[0] = 99
except TypeError as e:
    print("Error:", e)

