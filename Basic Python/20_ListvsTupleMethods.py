# 1. INITIALIZATION

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

print("List  :", my_list)
print("Tuple :", my_tuple)


# 2. append()

# LIST -> append() WORKS
# append() adds ONE element at the end.
# TUPLE -> append() DOES NOT WORK

my_list.append(40)
print("List  :", my_list)

try:
    my_tuple.append(40)
except AttributeError:
    print("Tuple : append() is INVALID")


# 3. extend()

# LIST -> extend() WORKS
# Adds multiple elements to the list at the end.

my_list.extend([50, 60])
print("List  :", my_list)

try:
    my_tuple.extend([40, 50])
except AttributeError:
    print("Tuple : extend() is INVALID")


# 4. insert()

# LIST -> insert() WORKS
# insert(index, value)

my_list.insert(1, 15)
print("List  :", my_list)

try:
    my_tuple.insert(1, 15)
except AttributeError:
    print("Tuple : insert() is INVALID")


# 5. remove()

# LIST -> remove() WORKS
# Removes the FIRST matching value.

my_list.remove(15)
print("List  :", my_list)

try:
    my_tuple.remove(20)
except AttributeError:
    print("Tuple : remove() is INVALID")


# 6. pop()

# LIST -> pop() WORKS
# Removes and returns the last element.

removed = my_list.pop()
print("List  :", my_list)

# TUPLE -> pop() DOES NOT WORK

try:
    my_tuple.pop()
except AttributeError:
    print("Tuple : pop() is INVALID")


# 7. clear()

# LIST -> clear() WORKS
# Removes ALL elements.

test_list = [10, 20, 30]

test_list.clear()

print("List  :", test_list)

# TUPLE -> clear() DOES NOT WORK

try:
    my_tuple.clear()
except AttributeError:
    print("Tuple : clear() is INVALID")


# 8. sort()

# LIST -> sort() WORKS
# Arranges the list in ascending order.

my_list = [40, 10, 30, 20]

my_list.sort()

print("List  :", my_list)

# TUPLE -> sort() DOES NOT WORK

my_tuple = (40, 10, 30, 20)

try:
    my_tuple.sort()
except AttributeError:
    print("Tuple : sort() is INVALID")


# 9. reverse()

# LIST -> reverse() WORKS
# Reverses the list.

my_list = [10, 20, 30, 40]

my_list.reverse()

print("List  :", my_list)

# TUPLE -> reverse() DOES NOT WORK

my_tuple = (10, 20, 30, 40)

try:
    my_tuple.reverse()
except AttributeError:
    print("Tuple : reverse() is INVALID")


# 10. copy()

# LIST -> copy() WORKS
# Creates a copy of the list.

my_list = [10, 20, 30]

new_list = my_list.copy()

print("Original List :", my_list)
print("Copied List   :", new_list)

# TUPLE -> copy() DOES NOT WORK

my_tuple = (10, 20, 30)

try:
    my_tuple.copy()
except AttributeError:
    print("Tuple : copy() is INVALID")


# 11. index()

# index() WORKS FOR BOTH LIST AND TUPLE
# Returns the index of the FIRST matching value.

# LIST

my_list = [10, 20, 30, 20]

position = my_list.index(20)

print("List Position :", position)


# TUPLE

my_tuple = (10, 20, 30, 20)

position = my_tuple.index(20)

print("Tuple Position:", position)


# 12. count()

# count() WORKS FOR BOTH LIST AND TUPLE
# Counts how many times a value occurs.

# LIST

my_list = [10, 20, 20, 30, 20]

result = my_list.count(20)

print("List Count :", result)


# TUPLE

my_tuple = (10, 20, 20, 30, 20)

result = my_tuple.count(20)

print("Tuple Count:", result)



# List is mutable, so we can add, remove, and modify elements.
# Tuple is immutable, so its elements cannot be changed.
# List has more methods, while Tuple mainly has count() and index().
# ============================================================