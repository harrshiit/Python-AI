# CLASS AND OBJECTS — MASTER EXAMPLE
# No constructor (__init__) or self yet.

# 1. DEFINING A CLASS

class Student:
    pass

# pass = placeholder for an intentionally empty class. Without a statement inside the class, Python gives:
# IndentationError: expected an indented block
# Java:
# class Student {
# }


# 2. CREATING AN OBJECT

student1 = Student()

print(student1)
# Output: <__main__.Student object at 0x...>Exact address will be different each time.
print(type(student1))
# Output: <class '__main__.Student'> student1 is an object/instance of Student.
#
# Java:
# Student student1 = new Student();

# MULTIPLE OBJECTS

student2 = Student() # defines a new object of the same class.
print(student1 is student2)
# Output: False  Same class, but two different objects.


# 4. CLASS ATTRIBUTES

class Student:
    school = "ABC School"
    country = "India"

student1 = Student()
student2 = Student()

# school and country are CLASS ATTRIBUTES.
# They belong to the class and are shared/default values.
#
# Java:
# class Student {
#     static String school = "ABC School";
#     static String country = "India";
# }


# 5. ACCESS CLASS ATTRIBUTES THROUGH CLASS

print(Student.school) # Output: ABC School
print(Student.country)# Output: India

# Student.attribute → direct access through CLASS.
#
# Java:
# System.out.println(Student.school);


# 6. ACCESS CLASS ATTRIBUTES THROUGH OBJECT
print(student1.school) # Output: ABC School
print(student2.school) # Output: ABC School

# Object can access a class attribute.
# Python roughly checks:
# student1.school → student1 first → Student class next. This is called ATTRIBUTE LOOKUP.


# 7. OBJECT / INSTANCE ATTRIBUTES

student1.name = "Harshit"
student1.age = 22
student2.name = "Rahul"
student2.age = 25

print(student1.name) # Output: Harshit
print(student1.age)# Output: 22
print(student2.name) # Output: Rahul
print(student2.age) # Output: 25

# name and age are OBJECT/INSTANCE ATTRIBUTES.
# Each object can have different data.
#
# Java:
# class Student {
#     String name;
#     int age;
# }


# 8. CLASS ATTRIBUTE VS OBJECT ATTRIBUTE

print(Student.school)# Output: ABC School
print(student1.school)# Output: ABC School
print(student1.name)# Output: Harshit
print(student2.name)# Output: Rahul

# Student.school → class perspective
# student1.school → object accessing class value
# student1.name → object-specific data


# 9. CHANGE AN OBJECT ATTRIBUTE

student1.age = 23

print(student1.age)# Output: 23
print(student2.age)# Output: 25
# Changing student1 does not affect student2.
# Each object has its own age.


# 10. CHANGE THE CLASS ATTRIBUTE

Student.school = "XYZ School"

print(Student.school)
# Output: XYZ School

print(student1.school)
# Output: XYZ School

print(student2.school)
# Output: XYZ School

# Both objects see the new class value because neither
# object has its own school attribute yet.


# 11. OBJECT OVERRIDES CLASS ATTRIBUTE

student1.school = "Private School"

print(student1.school)
# Output: Private School

print(student2.school)
# Output: XYZ School

print(Student.school)
# Output: XYZ School

# student1 now has its OWN school attribute.
#
# Student.school  → XYZ School
# student1.school → Private School
# student2.school → XYZ School
#
# student2 has no own school, so Python uses the class value.


# 12. CHANGE OBJECT ATTRIBUTE AGAIN

student1.school = "College School"

print(student1.school)
# Output: College School

print(student2.school)
# Output: XYZ School

print(Student.school)
# Output: XYZ School


# 13. OBJECT REFERENCE

student3 = student1

print(student1 is student3)
# Output: True
# student3 does not create a new object.
# Both variables refer to the SAME object.

student3.name = "Harshit Kumar"

print(student1.name)
# Output: Harshit Kumar

print(student3.name)
# Output: Harshit Kumar

# Changing through student3 also changes what student1 sees,
# because both refer to the same object.


# 14. FINAL STATE

print(Student.school)
# Output: XYZ School

print(student1.name)
# Output: Harshit Kumar

print(student1.age)
# Output: 23

print(student1.school)
# Output: College School

print(student2.name)
# Output: Rahul

print(student2.age)
# Output: 25

print(student2.school)
# Output: XYZ School


