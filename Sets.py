# ==============================================================
# 1. CREATING / INITIALIZING A SET
# ==============================================================

numbers = {10, 20, 30, 40}
print(numbers)
# OUTPUT: {10, 20, 30, 40}

# ==============================================================
# 2. EMPTY SET
# ==============================================================

empty_set = set()
print(empty_set)
# OUTPUT: set()

empty_dict = {}
print(empty_dict)
# OUTPUT: {}
# {} = EMPTY DICTIONARY, set() = EMPTY SET

# ==============================================================
# 3. set() CONSTRUCTOR
# ==============================================================

numbers = set([10, 20, 30, 40])
print(numbers)
# OUTPUT: {10, 20, 30, 40}

names = set(["Harshit", "Rahul", "Amit"])
print(names)
# OUTPUT: {'Harshit', 'Rahul', 'Amit'}
# Order may differ because sets are unordered.

# ==============================================================
# 4. DUPLICATE ELEMENTS
# ==============================================================

numbers = {10, 20, 20, 30, 30, 30}
print(numbers)
# OUTPUT: {10, 20, 30}
# Sets automatically remove duplicates.

# ==============================================================
# 5. SET IS UNORDERED
# ==============================================================

numbers = {10, 20, 30, 40, 50}
print(numbers)
# OUTPUT MAY BE: {40, 10, 50, 20, 30}
# OR another order. Do NOT depend on set order.

# ==============================================================
# 6. NO INDEXING / SLICING
# ==============================================================

numbers = {10, 20, 30}
# print(numbers[0])
# ❌ TypeError: 'set' object is not subscriptable
# Sets have no indexing or slicing.

# ==============================================================
# 7. SET IS MUTABLE
# ==============================================================

numbers = {10, 20, 30}
numbers.add(40)
print(numbers)
# OUTPUT: {10, 20, 30, 40}
# Set can be changed after creation.

# ==============================================================
# 8. add() METHOD
# ==============================================================

numbers = {10, 20, 30}
numbers.add(40)
print(numbers)
# OUTPUT: {10, 20, 30, 40}

numbers.add(20)
print(numbers)
# OUTPUT: {10, 20, 30, 40}
# Adding an existing element does nothing.

# ==============================================================
# 9. update() METHOD
# ==============================================================

numbers = {10, 20, 30}
numbers.update([40, 50, 60])
print(numbers)
# OUTPUT: {10, 20, 30, 40, 50, 60}
# update() adds multiple elements.

# ==============================================================
# 10. remove() METHOD
# ==============================================================

numbers = {10, 20, 30, 40}
numbers.remove(30)
print(numbers)
# OUTPUT: {10, 20, 40}

# numbers.remove(100)
# ❌ KeyError: 100
# remove() gives an error if element doesn't exist.

# ==============================================================
# 11. discard() METHOD
# ==============================================================

numbers = {10, 20, 30, 40}
numbers.discard(30)
print(numbers)
# OUTPUT: {10, 20, 40}

numbers.discard(100)
print(numbers)
# OUTPUT: {10, 20, 40}
# remove(100) -> KeyError
# discard(100) -> No error

# ==============================================================
# 12. pop() METHOD
# ==============================================================

numbers = {10, 20, 30, 40}
removed = numbers.pop()
print(removed)
# OUTPUT: One arbitrary element
print(numbers)
# OUTPUT: Remaining elements
# pop() removes an arbitrary element; exact element is not guaranteed.

# ==============================================================
# 13. clear() METHOD
# ==============================================================

numbers = {10, 20, 30}
numbers.clear()
print(numbers)
# OUTPUT: set()
# clear() removes all elements.

# ==============================================================
# 14. MEMBERSHIP TESTING
# ==============================================================

numbers = {10, 20, 30, 40}
print(20 in numbers)
# OUTPUT: True
print(100 in numbers)
# OUTPUT: False
print(100 not in numbers)
# OUTPUT: True
# "in" checks whether an element exists in the set.

# ==============================================================
# 15. len() FUNCTION
# ==============================================================

numbers = {10, 20, 30, 40}
print(len(numbers))
# OUTPUT: 4
# len() = number of elements.

# ==============================================================
# 16. LOOPING THROUGH SET
# ==============================================================

numbers = {10, 20, 30}
for number in numbers:
    print(number)
# OUTPUT:
# 10
# 20
# 30
# Order is NOT guaranteed.

# ==============================================================
# 17. UNION
# ==============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))
# OUTPUT: {1, 2, 3, 4, 5, 6}
# UNION = all unique elements from both sets.

# ==============================================================
# 18. UNION USING | OPERATOR
# ==============================================================

A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)
# OUTPUT: {1, 2, 3, 4, 5}
# A.union(B) == A | B

# ==============================================================
# 19. INTERSECTION
# ==============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.intersection(B))
# OUTPUT: {3, 4}
# INTERSECTION = common elements in both sets.

# ==============================================================
# 20. INTERSECTION USING & OPERATOR
# ==============================================================

A = {1, 2, 3}
B = {3, 4, 5}
print(A & B)
# OUTPUT: {3}
# A.intersection(B) == A & B

# ==============================================================
# 21. DIFFERENCE
# ==============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.difference(B))
# OUTPUT: {1, 2}
# A - B = elements in A but NOT in B.

print(B.difference(A))
# OUTPUT: {5, 6}
# B - A = elements in B but NOT in A.

# ==============================================================
# 22. DIFFERENCE USING - OPERATOR
# ==============================================================

A = {1, 2, 3}
B = {3, 4, 5}
print(A - B)
# OUTPUT: {1, 2}
# A.difference(B) == A - B

# ==============================================================
# 23. SYMMETRIC DIFFERENCE
# ==============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.symmetric_difference(B))
# OUTPUT: {1, 2, 5, 6}
# Elements in A OR B, but NOT in both.

# ==============================================================
# 24. SYMMETRIC DIFFERENCE USING ^ OPERATOR
# ==============================================================

A = {1, 2, 3}
B = {3, 4, 5}
print(A ^ B)
# OUTPUT: {1, 2, 4, 5}
# A.symmetric_difference(B) == A ^ B

# ==============================================================
# 25. SUBSET
# ==============================================================

A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))
# OUTPUT: True
# A is a subset of B if every element of A exists in B.

print(A <= B)
# OUTPUT: True
# <= can also check subset.

# ==============================================================
# 26. SUPERSET
# ==============================================================

A = {1, 2, 3, 4}
B = {1, 2}
print(A.issuperset(B))
# OUTPUT: True
# A is a superset of B if A contains every element of B.

print(A >= B)
# OUTPUT: True
# >= can also check superset.

# ==============================================================
# 27. DISJOINT SETS
# ==============================================================

A = {1, 2, 3}
B = {4, 5, 6}
print(A.isdisjoint(B))
# OUTPUT: True
# Disjoint = no common elements.

A = {1, 2, 3}
B = {3, 4, 5}
print(A.isdisjoint(B))
# OUTPUT: False

# ==============================================================
# 28. SET COMPARISON
# ==============================================================

A = {1, 2, 3}
B = {3, 2, 1}
print(A == B)
# OUTPUT: True
# Set order does NOT matter.

# ==============================================================
# 29. copy() METHOD
# ==============================================================

A = {1, 2, 3}
B = A.copy()
print(B)
# OUTPUT: {1, 2, 3}

# ==============================================================
# 30. DIFFERENT DATA TYPES AS SET ELEMENTS
# ==============================================================

data = {10, 3.14, "Python", True, (1, 2)}
print(data)
# OUTPUT: Order may differ.
# Example: {True, 3.14, 10, 'Python', (1, 2)}
# Set elements must be HASHABLE.

# ==============================================================
# 31. LIST CANNOT BE SET ELEMENT
# ==============================================================

# wrong = {[1, 2, 3]}
# ❌ TypeError: unhashable type: 'list'
# List is mutable, so it cannot be a set element.

# ==============================================================
# 32. TUPLE CAN BE SET ELEMENT
# ==============================================================

data = {(1, 2), (3, 4)}
print(data)
# OUTPUT: {(1, 2), (3, 4)}
# Tuple can be a set element if all its elements are hashable.

# ==============================================================
# 33. FROZENSET
# ==============================================================

numbers = frozenset([1, 2, 3, 4])
print(numbers)
# OUTPUT: frozenset({1, 2, 3, 4})
# set -> mutable
# frozenset -> immutable

# ==============================================================
# 34. SET COMPREHENSION
# ==============================================================

squares = {x * x for x in range(1, 6)}
print(squares)
# OUTPUT: {1, 4, 9, 16, 25}
# Syntax: {expression for item in iterable}

# ==============================================================
# 35. SET COMPREHENSION WITH CONDITION
# ==============================================================

even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print(even_numbers)
# OUTPUT: {2, 4, 6, 8, 10}

# ==============================================================
# 36. REMOVE DUPLICATES FROM LIST
# ==============================================================

numbers = [1, 2, 2, 3, 3, 4, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)
# OUTPUT: {1, 2, 3, 4}
# One of the most common uses of sets.

# ==============================================================
# 37. CONVERT SET TO LIST
# ==============================================================

numbers = {1, 2, 3, 4}
numbers_list = list(numbers)
print(numbers_list)
# OUTPUT: [1, 2, 3, 4]
# Order should NOT be relied upon.

# ==============================================================
# 38. FIND COMMON ELEMENTS BETWEEN TWO LISTS
# ==============================================================

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(common)
# OUTPUT: {4, 5}

# ==============================================================
# 39. DETECT DUPLICATES
# ==============================================================

numbers = [1, 2, 3, 2]
if len(numbers) != len(set(numbers)):
    print("Duplicates exist")
else:
    print("No duplicates")
# OUTPUT: Duplicates exist

# ==============================================================
# 40. DSA - DUPLICATE DETECTION
# ==============================================================

numbers = [1, 2, 3, 4, 2]
seen = set()

for num in numbers:
    if num in seen:
        print("Duplicate:", num)
        break
    seen.add(num)

# OUTPUT: Duplicate: 2
# Set is useful for fast lookup of already-seen values.

# ==============================================================
# 41. PRACTICAL EXAMPLE - STUDENTS
# ==============================================================

python_students = {"Harshit", "Rahul", "Amit", "Priya"}
java_students = {"Rahul", "Priya", "Ankit"}

both = python_students & java_students
print(both)
# OUTPUT: {'Rahul', 'Priya'}

both_courses = python_students | java_students
print(both_courses)
# OUTPUT: {'Harshit', 'Rahul', 'Amit', 'Priya', 'Ankit'}

only_python = python_students - java_students
print(only_python)
# OUTPUT: {'Harshit', 'Amit'}

only_java = java_students - python_students
print(only_java)
# OUTPUT: {'Ankit'}

# ==============================================================
# 42. PERMISSION / SUBSET EXAMPLE
# ==============================================================

required = {"read", "write", "delete"}
user_permissions = {"read", "write"}

print(required.issubset(user_permissions))
# OUTPUT: False

missing = required - user_permissions
print(missing)
# OUTPUT: {'delete'}


# 44. SET OPERATORS - QUICK REVISION
# ==============================================================

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
# UNION -> {1, 2, 3, 4, 5}

print(A & B)
# INTERSECTION -> {3}

print(A - B)
# DIFFERENCE -> {1, 2}

print(A ^ B)
