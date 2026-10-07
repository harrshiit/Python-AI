# ================================================================
#              TUPLE & LIST UNPACKING
# ================================================================


# 1. BASIC TUPLE UNPACKING
# Values from a tuple are assigned to separate variables.
# Number of variables should normally match number of values.

data = (10, 20, 30)

a, b, c = data

print(a, b, c)
# RESULT:
# 10 20 30


# 2. TUPLE UNPACKING WITHOUT PARENTHESES
# Parentheses are not required when unpacking.

a, b, c = 10, 20, 30

print(a, b, c)
# RESULT:
# 10 20 30


# 3. LIST UNPACKING
# Lists can also be unpacked into separate variables.

data = [10, 20, 30]

a, b, c = data

print(a, b, c)
# RESULT:
# 10 20 30


# 4. UNPACKING STRING
# Strings are iterable, so characters can be unpacked.

a, b, c = "ABC"

print(a, b, c)
# RESULT:
# A B C


# 5. UNPACKING DIFFERENT DATA TYPES
# Each value is assigned to one variable.

data = ("Rahul", 20, 85.5)

name, age, marks = data

print(name, age, marks)
# RESULT:
# Rahul 20 85.5


# 6. UNPACKING NESTED TUPLE
# Nested structures can also be unpacked.

data = ("Rahul", (20, "Python"))

name, (age, course) = data

print(name, age, course)
# RESULT:
# Rahul 20 Python


# 7. UNPACKING NESTED LIST
# Nested lists can be unpacked in the same way.

data = ["Rahul", [20, "Python"]]

name, [age, course] = data

print(name, age, course)
# RESULT:
# Rahul 20 Python


# 8. MIXED NESTED UNPACKING
# Tuple and list can be mixed during unpacking.

data = ("Rahul", [20, "Python"])

name, [age, course] = data

print(name, age, course)
# RESULT:
# Rahul 20 Python


# ================================================================
#              EXTENDED UNPACKING (*)
# ================================================================

# 9. STARRED VARIABLE
# * collects multiple remaining values into a LIST.

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
# RESULT:
# 10

print(middle)
# RESULT:
# [20, 30, 40]

print(last)
# RESULT:
# 50


# 10. STARRED VARIABLE AT THE END
# * collects all remaining values after the first variable.

numbers = (10, 20, 30, 40, 50)

first, *remaining = numbers

print(first)
# RESULT:
# 10

print(remaining)
# RESULT:
# [20, 30, 40, 50]


# 11. STARRED VARIABLE AT THE BEGINNING
# * collects all values except the last one.

numbers = (10, 20, 30, 40, 50)

*beginning, last = numbers

print(beginning)
# RESULT:
# [10, 20, 30, 40]

print(last)
# RESULT:
# 50


# 12. STARRED VARIABLE IN THE MIDDLE
# * collects the values between the first and last variables.

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first, middle, last)
# RESULT:
# 10 [20, 30, 40] 50


# 13. STARRED VARIABLE WITH ONLY TWO VALUES
# The starred variable can receive an empty list.

numbers = (10, 20)

first, *middle, last = numbers

print(first, middle, last)
# RESULT:
# 10 [] 20


# 14. STARRED VARIABLE WITH ONE VALUE
# The starred variable receives an empty list.

numbers = (10,)

# first, *middle = numbers

print(numbers)
# RESULT:
# (10,)

# Example:
# first, *middle = (10,)
#
# first = 10
# middle = []


# ================================================================
#              UNPACKING LIST AND TUPLE TOGETHER
# ================================================================

# 15. LIST -> VARIABLES

data = [10, 20, 30]

a, b, c = data

print(a, b, c)
# RESULT:
# 10 20 30


# 16. TUPLE -> VARIABLES

data = (10, 20, 30)

a, b, c = data

print(a, b, c)
# RESULT:
# 10 20 30


# 17. RANGE -> VARIABLES
# Any iterable can be unpacked if the number of values matches.

a, b, c = range(1, 4)

print(a, b, c)
# RESULT:
# 1 2 3


# 18. STRING -> VARIABLES

a, b, c, d = "CODE"

print(a, b, c, d)
# RESULT:
# C O D E


# ================================================================
#              UNPACKING IN LOOPS
# ================================================================

# 19. LIST OF TUPLES
# Each tuple is unpacked during every loop iteration.

students = [
    ("Rahul", 20),
    ("Amit", 21),
    ("Priya", 19)
]

for name, age in students:
    print(name, age)

# RESULT:
# Rahul 20
# Amit 21
# Priya 19


# 20. LIST OF LISTS
# Each inner list is unpacked during the loop.

students = [
    ["Rahul", 20],
    ["Amit", 21],
    ["Priya", 19]
]

for name, age in students:
    print(name, age)

# RESULT:
# Rahul 20
# Amit 21
# Priya 19


# 21. LOOP WITH THREE VALUES

students = [
    ("Rahul", 20, "Python"),
    ("Amit", 21, "Java")
]

for name, age, course in students:
    print(name, age, course)

# RESULT:
# Rahul 20 Python
# Amit 21 Java


# ================================================================
#              FUNCTION RETURN UNPACKING
# ================================================================

# 22. FUNCTION RETURNING MULTIPLE VALUES
# Multiple return values are normally returned as a tuple.
# The result can immediately be unpacked.

def get_student():
    return "Rahul", 20, "Python"


name, age, course = get_student()

print(name, age, course)
# RESULT:
# Rahul 20 Python


# 23. FUNCTION + STARRED UNPACKING

def get_numbers():
    return 10, 20, 30, 40, 50


first, *remaining = get_numbers()

print(first)
# RESULT:
# 10

print(remaining)
# RESULT:
# [20, 30, 40, 50]


# ================================================================
#              VARIABLE SWAPPING
# ================================================================

# 24. SWAPPING TWO VARIABLES
# Python uses packing + unpacking internally.
#
# a, b = b, a
#
# Right side is packed:
# (b, a)
#
# Left side is unpacked:
# a, b

a = 10
b = 20

a, b = b, a

print(a, b)
# RESULT:
# 20 10


# 25. SWAPPING THREE VARIABLES

a = 10
b = 20
c = 30

a, b, c = c, a, b

print(a, b, c)
# RESULT:
# 30 10 20


# ================================================================
#              IGNORING VALUES
# ================================================================

# 26. USING _ TO IGNORE A VALUE
# _ is commonly used when you don't need a value.

data = (10, 20, 30)

a, _, c = data

print(a, c)
# RESULT:
# 10 30


# 27. IGNORING MULTIPLE VALUES WITH *
# * can collect values that you don't need.

data = (10, 20, 30, 40, 50)

first, *_, last = data

print(first, last)
# RESULT:
# 10 50

print(_)
# RESULT:
# [20, 30, 40]


# ================================================================
#              DICTIONARY UNPACKING
# ================================================================

# 28. UNPACKING DICTIONARY KEYS
# Iterating/unpacking a dictionary directly gives its KEYS.

data = {"name": "Rahul", "age": 20}

a, b = data

print(a, b)
# RESULT:
# name age


# 29. UNPACKING DICTIONARY ITEMS
# items() produces key-value tuples which can be unpacked.

data = {"name": "Rahul", "age": 20}

for key, value in data.items():
    print(key, value)

# RESULT:
# name Rahul
# age 20


# ================================================================
#              UNPACKING WITH *
# ================================================================

# 30. UNPACKING INTO A FUNCTION
# * passes list/tuple elements as separate arguments.

def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

result = add(*numbers)

print(result)
# RESULT:
# 60


# 31. TUPLE INTO FUNCTION ARGUMENTS

numbers = (10, 20, 30)

result = add(*numbers)

print(result)
# RESULT:
# 60


# ================================================================
#              IMPORTANT ERRORS
# ================================================================

# 32. TOO FEW VARIABLES
# Number of variables must match the iterable,
# unless * is used.

# a, b = (10, 20, 30)
#
# RESULT:
# ValueError: too many values to unpack


# 33. TOO MANY VARIABLES

# a, b, c, d = (10, 20, 30)
#
# RESULT:
# ValueError: not enough values to unpack


# 34. SOLUTION USING *
# * allows extra values to be collected.

a, *b = (10, 20, 30)

print(a, b)
# RESULT:
# 10 [20, 30]


# ================================================================
#              IMPORTANT FEATURES
# ================================================================

# 35. NORMAL UNPACKING
data = (10, 20, 30)
a, b, c = data

print(a, b, c)
# RESULT:
# 10 20 30


# 36. EXTENDED UNPACKING
data = (10, 20, 30, 40)
a, *b = data

print(a, b)
# RESULT:
# 10 [20, 30, 40]


# 37. NESTED UNPACKING
data = ("Rahul", (20, "Python"))

name, (age, course) = data

print(name, age, course)
# RESULT:
# Rahul 20 Python


# 38. LOOP UNPACKING
for name, age in [("Rahul", 20), ("Amit", 21)]:
    print(name, age)

# RESULT:
# Rahul 20
# Amit 21


# 39. FUNCTION UNPACKING
def get_data():
    return 10, 20, 30

a, b, c = get_data()

print(a, b, c)
# RESULT:
# 10 20 30


# 40. SWAPPING
a = 10
b = 20

a, b = b, a

print(a, b)
# RESULT:
# 20 10


# ================================================================
#              QUICK MEMORY
# ================================================================

# NORMAL UNPACKING
a, b, c = (10, 20, 30)
# RESULT:
# a = 10
# b = 20
# c = 30


# LIST UNPACKING
a, b, c = [10, 20, 30]
# RESULT:
# a = 10
# b = 20
# c = 30


# STAR UNPACKING
a, *b = [10, 20, 30, 40]
# RESULT:
# a = 10
# b = [20, 30, 40]


# MIDDLE STAR UNPACKING
a, *b, c = [10, 20, 30, 40]
# RESULT:
# a = 10
# b = [20, 30]
# c = 40


# SWAPPING
a, b = b, a
# RESULT:
# Values of a and b are exchanged