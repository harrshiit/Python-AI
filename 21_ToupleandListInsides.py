# ============================================================
#       MUTABILITY: LIST INSIDE TUPLE & TUPLE INSIDE LIST
# ============================================================


# ============================================================
# 1. LIST INSIDE TUPLE
# ============================================================

my_tuple = (10, 20, [30, 40])

print("Original Tuple:", my_tuple)


# Tuple is IMMUTABLE
# We cannot change the tuple's elements.

# my_tuple[0] = 100
# ❌ ERROR: Tuple does not support item assignment


# But the List inside the Tuple is MUTABLE.
# Therefore, we CAN change the List.

my_tuple[2].append(50)

print("After append:", my_tuple)


# We can also change an element of the List.

my_tuple[2][0] = 300

print("After changing List element:", my_tuple)


# But we CANNOT replace the List itself.

# my_tuple[2] = [60, 70]
# ❌ ERROR: Tuple is immutable


# ============================================================
# 2. TUPLE INSIDE LIST
# ============================================================

my_list = [10, 20, (30, 40)]

print("\nOriginal List:", my_list)


# List is MUTABLE.
# Therefore, we CAN change its elements.

my_list[0] = 100

print("After changing List element:", my_list)


# We can also replace the Tuple inside the List.

my_list[2] = (50, 60)

print("After replacing Tuple:", my_list)


# But the Tuple inside the List is IMMUTABLE.
# Therefore, we CANNOT change an element inside the Tuple.

# my_list[2][0] = 500
# ❌ ERROR: Tuple does not support item assignment


# ============================================================
# 3. SIMPLE COMPARISON
# ============================================================

# Tuple containing List:
#
# Outer Tuple  -> IMMUTABLE
# Inner List   -> MUTABLE
#
# my_tuple = (10, 20, [30, 40])
#
# my_tuple[2].append(50)  -> VALID
# my_tuple[2][0] = 300    -> VALID
# my_tuple[2] = [50, 60]  -> INVALID


# List containing Tuple:
#
# Outer List   -> MUTABLE
# Inner Tuple  -> IMMUTABLE
#
# my_list = [10, 20, (30, 40)]
#
# my_list[0] = 100        -> VALID
# my_list[2] = (50, 60)   -> VALID
# my_list[2][0] = 500     -> INVALID


# ============================================================
# CONCLUSION
# ============================================================

# Tuple cannot change its own elements, but a List inside it
# can still be modified because the List itself is mutable.
# A List can change its elements, but a Tuple inside it
# remains immutable.
# ============================================================