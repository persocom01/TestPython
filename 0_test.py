import re

text = '''abs()	Absolute value
sin(), cos(), tan()	Standard trigonometric functions; with the argument in radians.
asin(), acos(), atan(), atan2()	Inverse trigonometric functions; return values in radians.
sinh(), cosh(), tanh()	Hyperbolic functions; argument in hyperbolic angle.
asinh(), acosh(), atanh()	Inverse hyperbolic functions; return values in hyperbolic angle.
pow(), exp(), expm1(), log10(), log1p(), log2()

Exponential and logarithmic functions.
floor(), ceil()	Returns the largest/smallest integer less/greater than or equal to an argument.
min(), max()	Returns the minimum or maximum (respectively) value of a comma separated list of numbers as arguments.
random()	Returns a random number between 0 and 1.
round(), fround(), trunc(),	Rounding and truncation functions.
sqrt(), cbrt(), hypot()	Square root, cube root, Square root of the sum of square arguments.
sign()	The sign of a number, indicating whether the number is positive, negative or zero.
clz32(),
imul()	Number of leading zero bits in the 32-bit binary representation.
The result of the C-like 32-bit multiplication of the two arguments.'''

numbers = re.findall(
    r'(\w+)\(\)', text, re.I | re.M)

output = []
for num in numbers:
    output.append(r'console.log(' + '\'' + num +
                  r':' + '\'' + ', Math.' + num + r'())')

print('\n'.join(output))
