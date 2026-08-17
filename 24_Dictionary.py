# 1. CREATING / INITIALIZING A DICTIONARY
# ==============================================================

# Empty dictionary
d1 = {}
print(d1)
# OUTPUT: {}

# Dictionary with data
student = {
    "name": "Harshit",
    "age": 22,
    "course": "CSE",
    "cgpa": 7.5
}
print(student)
# OUTPUT: {'name': 'Harshit', 'age': 22, 'course': 'CSE', 'cgpa': 7.5}

# Using dict() constructor
student2 = dict(name="Rahul", age=23, course="CSE")
print(student2)
# OUTPUT: {'name': 'Rahul', 'age': 23, 'course': 'CSE'}


# ==============================================================
# 2. KEY-VALUE STRUCTURE
# ==============================================================

student = {
    "name": "Harshit",
    "age": 22
}

# "name"   -> KEY
# "Harshit" -> VALUE
# "age"    -> KEY
# 22       -> VALUE


# ==============================================================
# 3. ACCESSING VALUES
# ==============================================================

print(student["name"])
# OUTPUT: Harshit

print(student["age"])
# OUTPUT: 22


# ==============================================================
# 4. get() METHOD
# ==============================================================

print(student.get("name"))
# OUTPUT: Harshit

print(student.get("city"))
# OUTPUT: None

print(student.get("city", "Not Available"))
# OUTPUT: Not Available

# student["city"] -> KeyError
# student.get("city") -> None


# ==============================================================
# 5. ADDING & UPDATING VALUES
# ==============================================================

student["city"] = "Kanpur"       # ADD
student["age"] = 23              # UPDATE

print(student)
# OUTPUT: {'name': 'Harshit', 'age': 23, 'city': 'Kanpur'}


# ==============================================================
# 6. update() METHOD
# ==============================================================

student.update({
    "age": 24,
    "city": "Delhi",
    "phone": "9999999999"
})

print(student)
# OUTPUT: {'name': 'Harshit', 'age': 24,
#          'city': 'Delhi', 'phone': '9999999999'}


# ==============================================================
# 7. keys() METHOD
# ==============================================================

print(student.keys())
# OUTPUT: dict_keys(['name', 'age', 'city', 'phone'])


# ==============================================================
# 8. values() METHOD
# ==============================================================

print(student.values())
# OUTPUT: dict_values(['Harshit', 24, 'Delhi', '9999999999'])


# ==============================================================
# 9. items() METHOD
# ==============================================================

print(student.items())
# OUTPUT: dict_items([
# ('name', 'Harshit'),
# ('age', 24),
# ('city', 'Delhi'),
# ('phone', '9999999999')
# ])


# ==============================================================
# 10. LOOPING THROUGH DICTIONARY
# ==============================================================

# Keys
for key in student:
    print(key)

# OUTPUT:
# name
# age
# city
# phone


# Values
for value in student.values():
    print(value)

# OUTPUT:
# Harshit
# 24
# Delhi
# 9999999999


# Keys + Values
for key, value in student.items():
    print(key, ":", value)

# OUTPUT:
# name : Harshit
# age : 24
# city : Delhi
# phone : 9999999999


# ==============================================================
# 11. CHECKING EXISTENCE
# ==============================================================

print("name" in student)
# OUTPUT: True

print("salary" in student)
# OUTPUT: False

print("salary" not in student)
# OUTPUT: True

# "in" checks KEYS.


# ==============================================================
# 12. len() FUNCTION
# ==============================================================

print(len(student))
# OUTPUT: 4

# len() = number of key-value pairs


# ==============================================================
# 13. pop() METHOD
# ==============================================================

removed = student.pop("phone")

print(removed)
# OUTPUT: 9999999999

print(student)
# OUTPUT: {'name': 'Harshit', 'age': 24, 'city': 'Delhi'}


# ==============================================================
# 14. popitem() METHOD
# ==============================================================

student["course"] = "CSE"

student.popitem()

print(student)
# OUTPUT: {'name': 'Harshit', 'age': 24, 'city': 'Delhi'}

# Removes the LAST inserted key-value pair.


# ==============================================================
# 15. setdefault() METHOD
# ==============================================================

student.setdefault("age", 30)
print(student["age"])
# OUTPUT: 24

student.setdefault("course", "CSE")
print(student)
# OUTPUT: {'name': 'Harshit', 'age': 24,
#          'city': 'Delhi', 'course': 'CSE'}

# Existing key -> no change
# Missing key -> creates key


# ==============================================================
# 16. copy() METHOD
# ==============================================================

student_copy = student.copy()

print(student_copy)
# OUTPUT: {'name': 'Harshit', 'age': 24,
#          'city': 'Delhi', 'course': 'CSE'}


# ==============================================================
# 17. fromkeys() METHOD
# ==============================================================

keys = ["name", "age", "city"]

d = dict.fromkeys(keys)
print(d)
# OUTPUT: {'name': None, 'age': None, 'city': None}

d = dict.fromkeys(keys, "Unknown")
print(d)
# OUTPUT: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}


# ==============================================================
# 18. clear() METHOD
# ==============================================================

d = {"a": 10, "b": 20, "c": 30}

d.clear()

print(d)
# OUTPUT: {}


# ==============================================================
# 19. DUPLICATE KEYS
# ==============================================================

d = {
    "name": "Harshit",
    "name": "Rahul"
}

print(d)
# OUTPUT: {'name': 'Rahul'}

# Keys MUST be unique.
# Latest value replaces previous value.


# ==============================================================
# 20. DUPLICATE VALUES
# ==============================================================

d = {
    "student1": "CSE",
    "student2": "CSE",
    "student3": "CSE"
}

print(d)
# OUTPUT: {'student1': 'CSE', 'student2': 'CSE', 'student3': 'CSE'}

# Values CAN be duplicated.


# ==============================================================
# 21. DIFFERENT DATA TYPES AS VALUES
# ==============================================================

data = {
    "name": "Harshit",              # String
    "age": 22,                      # Integer
    "cgpa": 7.5,                    # Float
    "passed": True,                 # Boolean
    "skills": ["Python", "Java"],   # List
    "location": ("UP", "India")     # Tuple
}

print(data)
# OUTPUT: {
# 'name': 'Harshit',
# 'age': 22,
# 'cgpa': 7.5,
# 'passed': True,
# 'skills': ['Python', 'Java'],
# 'location': ('UP', 'India')
# }


# ==============================================================
# 22. LIST / TUPLE / DICTIONARY AS VALUES
# ==============================================================

student = {
    "name": "Harshit",
    "skills": ["Python", "Java", "SQL"],
    "location": ("Kanpur", "UP"),
    "address": {
        "city": "Kanpur",
        "country": "India"
    }
}

print(student["skills"])
# OUTPUT: ['Python', 'Java', 'SQL']

print(student["skills"][0])
# OUTPUT: Python

print(student["location"][0])
# OUTPUT: Kanpur

print(student["address"]["city"])
# OUTPUT: Kanpur


# ==============================================================
# 23. NESTED DICTIONARY
# ==============================================================

students = {
    "student1": {
        "name": "Harshit",
        "age": 22
    },
    "student2": {
        "name": "Rahul",
        "age": 23
    }
}

print(students["student1"]["name"])
# OUTPUT: Harshit

print(students["student2"]["age"])
# OUTPUT: 23


# ==============================================================
# 24. LIST OF DICTIONARIES
# ==============================================================

students = [
    {"name": "Harshit", "age": 22},
    {"name": "Rahul", "age": 23}
]

print(students[0]["name"])
# OUTPUT: Harshit

print(students[1]["age"])
# OUTPUT: 23


# ==============================================================
# 25. DICTIONARY COMPREHENSION
# ==============================================================

squares = {i: i * i for i in range(1, 6)}

print(squares)
# OUTPUT: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# With condition
even_squares = {
    i: i * i
    for i in range(1, 11)
    if i % 2 == 0
}

print(even_squares)
# OUTPUT: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# ==============================================================
# 26. SWAPPING KEYS & VALUES
# ==============================================================

d = {"a": 1, "b": 2, "c": 3}

swapped = {
    value: key
    for key, value in d.items()
}

print(swapped)
# OUTPUT: {1: 'a', 2: 'b', 3: 'c'}


# ==============================================================
# 27. DIFFERENT TYPES OF KEYS
# ==============================================================

d = {
    "name": "Harshit",
    1: "One",
    2.5: "Float",
    (1, 2): "Tuple"
}

print(d["name"])
# OUTPUT: Harshit

print(d[1])
# OUTPUT: One

print(d[(1, 2)])
# OUTPUT: Tuple

# Keys must be HASHABLE.


# ==============================================================
# 28. LIST CANNOT BE A KEY
# ==============================================================

# d = {
#     [1, 2]: "Hello"
# }

# OUTPUT:
# TypeError: unhashable type: 'list'


# ==============================================================
# 29. del STATEMENT
# ==============================================================

d = {
    "name": "Harshit",
    "age": 22,
    "city": "Kanpur"
}

del d["age"]

print(d)
# OUTPUT: {'name': 'Harshit', 'city': 'Kanpur'}

# del is NOT a dictionary method.


# ==============================================================
# 30. FREQUENCY COUNT - IMPORTANT FOR DSA
# ==============================================================

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)
# OUTPUT: {1: 1, 2: 2, 3: 3, 4: 4}
