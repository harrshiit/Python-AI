# ================================================================
#              TUPLE PACKING
# ================================================================

# 1. BASIC TUPLE PACKING
# Multiple values separated by commas are packed into a tuple.
# The COMMA is what makes a tuple.

tuple1 = 10, 20, 30

print(tuple1)
# RESULT:
# (10, 20, 30)


# 2. TUPLE PACKING WITH PARENTHESES
# Parentheses are optional for tuple packing.
# Both forms create the same type of object.

tuple2 = (10, 20, 30)

print(tuple2)
# RESULT:
# (10, 20, 30)


# 3. PACKING VARIABLES INTO A TUPLE
# Values stored in variables can be packed into one tuple.

name = "Rahul"
age = 20
course = "Python"

student = name, age, course

print(student)
# RESULT:
# ('Rahul', 20, 'Python')


# 4. PACKING EXPRESSIONS INTO A TUPLE
# Expressions/calculations can also be packed.

a = 10
b = 5

result = a + b, a - b, a * b, a / b

print(result)
# RESULT:
# (15, 5, 50, 2.0)


# 5. MIXED DATA TYPES IN A TUPLE
# A tuple can contain different data types.

mixed = ("Rahul", 20, 85.5, True, [10, 20], {"city": "Delhi"})

print(mixed)
# RESULT:
# ('Rahul', 20, 85.5, True, [10, 20], {'city': 'Delhi'})


# 6. ONE-ELEMENT TUPLE
# (10)  -> integer
# (10,) -> tuple
# The COMMA creates the tuple.

x = (10)
y = (10,)

print(x, type(x))
# RESULT:
# 10 <class 'int'>

print(y, type(y))
# RESULT:
# (10,) <class 'tuple'>


# 7. TUPLE WITHOUT PARENTHESES
# Parentheses are not required when commas are present.

languages = "Python", "Java", "C++"

print(languages)
# RESULT:
# ('Python', 'Java', 'C++')


# 8. NESTED TUPLE
# A tuple can contain another tuple.

data = ("Rahul", (20, "Python"), (90, 85, 95))

print(data)
# RESULT:
# ('Rahul', (20, 'Python'), (90, 85, 95))


# 9. TUPLE CONTAINING A LIST
# A tuple can contain mutable objects such as lists.

data = ("Rahul", 20, ["Python", "Java"])

print(data)
# RESULT:
# ('Rahul', 20, ['Python', 'Java'])


# 10. FUNCTION RETURNING MULTIPLE VALUES
# Multiple returned values are packed into a tuple.

def student_data():
    return "Rahul", 20, "Python"

data = student_data()

print(data)
# RESULT:
# ('Rahul', 20, 'Python')

print(type(data))
# RESULT:
# <class 'tuple'>


# ================================================================
#              LIST PACKING / LIST CREATION
# ================================================================

# 11. BASIC LIST
# Multiple values are grouped into a list using [].

numbers = [10, 20, 30, 40]

print(numbers)
# RESULT:
# [10, 20, 30, 40]


# 12. LIST WITH VARIABLES
# Variables can be grouped into a list.

name = "Rahul"
age = 20
course = "Python"

student = [name, age, course]

print(student)
# RESULT:
# ['Rahul', 20, 'Python']


# 13. LIST WITH EXPRESSIONS
# Calculated values can be stored in a list.

a = 10
b = 5

result = [a + b, a - b, a * b, a / b]

print(result)
# RESULT:
# [15, 5, 50, 2.0]


# 14. MIXED DATA TYPES IN A LIST
# A list can contain different data types.

data = ["Rahul", 20, 85.5, True, (10, 20), {"city": "Delhi"}]

print(data)
# RESULT:
# ['Rahul', 20, 85.5, True, (10, 20), {'city': 'Delhi'}]


# 15. NESTED LIST
# A list can contain other lists.

matrix = [[1, 2], [3, 4], [5, 6]]

print(matrix)
# RESULT:
# [[1, 2], [3, 4], [5, 6]]


# 16. LIST CONTAINING TUPLES
# Very common for storing records.

students = [("Rahul", 20), ("Amit", 21), ("Priya", 19)]

print(students)
# RESULT:
# [('Rahul', 20), ('Amit', 21), ('Priya', 19)]


# ================================================================
#              CONVERSION / ITERABLE PACKING
# ================================================================

# 17. TUPLE -> LIST USING list()
# list() converts an iterable into a list.

data = list((10, 20, 30))

print(data)
# RESULT:
# [10, 20, 30]


# 18. STRING -> LIST
# A string is iterable, so each character becomes an item.

letters = list("Python")

print(letters)
# RESULT:
# ['P', 'y', 't', 'h', 'o', 'n']


# 19. LIST -> TUPLE USING tuple()
# tuple() converts an iterable into a tuple.

data = tuple([10, 20, 30])

print(data)
# RESULT:
# (10, 20, 30)


# 20. STRING -> TUPLE
# Each character becomes an item of the tuple.

letters = tuple("Python")

print(letters)
# RESULT:
# ('P', 'y', 't', 'h', 'o', 'n')


# 21. RANGE -> LIST
# list() converts range values into a list.

numbers = list(range(1, 6))

print(numbers)
# RESULT:
# [1, 2, 3, 4, 5]


# 22. RANGE -> TUPLE
# tuple() converts range values into a tuple.

numbers = tuple(range(1, 6))

print(numbers)
# RESULT:
# (1, 2, 3, 4, 5)


# ================================================================
#              STAR (*) PACKING
# ================================================================

# 23. STAR PACKING INTO A LIST
# * takes elements from another iterable and inserts them
# individually into the new list.

numbers = [1, 2, 3]

result = [*numbers, 4, 5]

print(result)
# RESULT:
# [1, 2, 3, 4, 5]


# 24. STAR PACKING INTO A TUPLE
# * can also insert elements into a new tuple.

numbers = [1, 2, 3]

result = (*numbers, 4, 5)

print(result)
# RESULT:
# (1, 2, 3, 4, 5)


# 25. COMBINING TWO LISTS USING *
# * can combine elements from multiple iterables.

a = [1, 2, 3]
b = [4, 5, 6]

result = [*a, *b]

print(result)
# RESULT:
# [1, 2, 3, 4, 5, 6]


# 26. COMBINING TWO TUPLES USING *

a = (1, 2, 3)
b = (4, 5, 6)

result = (*a, *b)

print(result)
# RESULT:
# (1, 2, 3, 4, 5, 6)


# 27. STAR + NORMAL VALUES
# * can be placed between normal values.

numbers = [2, 3, 4]

result = [1, *numbers, 5]

print(result)
# RESULT:
# [1, 2, 3, 4, 5]


# ================================================================
#              LIST COMPREHENSION
# ================================================================

# 28. LIST COMPREHENSION
# A compact way to create a list from an expression.

squares = [x * x for x in range(1, 6)]

print(squares)
# RESULT:
# [1, 4, 9, 16, 25]
