# POINT 01 - WHAT IS A CLASS METHOD?
# A class method receives the CLASS itself as the first argument. @classmethod is used and first parameter is conventionally "cls". self -> current OBJECT | cls -> current CLASS
class Point01_Student:
    college = "GCET"

    @classmethod
    def show_college(cls):
        print(cls.college)

Point01_Student.show_college()  # OUTPUT: GCET


# POINT 02 - WHY DO WE NEED CLASS METHOD?
# Class-level data belongs to the CLASS, not a particular object.
# So we don't need an object; classmethod performs class-level operations.
class Point02_College:
    college = "GCET"
    @classmethod
    def show_college(cls):
        print("College:", cls.college)
Point02_College.show_college()  # OUTPUT: College: GCET

# POINT 03 - WHAT IS "cls"?
# cls is the current CLASS, just like self is the current OBJECT. "cls" is a convention, not a Python keyword.
class Point03_Demo:
    @classmethod
    def show(cls):
        print(cls.__name__)
Point03_Demo.show()  # OUTPUT: Point03_Demo

# POINT 04 - SELF VS CLS
# self -> current object | cls -> current class
class Point04_Student:
    def show_instance(self):
        print("self:", type(self).__name__)
    @classmethod
    def show_class(cls):
        print("cls:", cls.__name__)
s = Point04_Student()
s.show_instance()          # OUTPUT: self: Point04_Student
Point04_Student.show_class()  # OUTPUT: cls: Point04_Student

# POINT 05 - INSTANCE METHOD INTERNAL WORKFLOW
# s.show() is internally similar to Point05_Student.show(s).
# Therefore Python automatically passes the object as self.
class Point05_Student:
    def show(self):
        print("Hello")
s = Point05_Student()
s.show()  # OUTPUT: Hello

# POINT 06 - CLASS METHOD INTERNAL WORKFLOW
# Student.show() is conceptually similar to Student.show(Student).
# Therefore Python automatically passes the class as cls.
class Point06_Student:
    @classmethod
    def show(cls):
        print(cls.__name__)
Point06_Student.show()  # OUTPUT: Point06_Student

# POINT 07 - CALL CLASS METHOD USING CLASS
# Most common way: ClassName.method()
class Point07_Student:
    college = "GCET"
    @classmethod
    def show_college(cls):
        print(cls.college)
Point07_Student.show_college()  # OUTPUT: GCET

# POINT 08 - CALL CLASS METHOD USING OBJECT
# Object can call a class method, but cls is still the CLASS, not object.
class Point08_Student:
    @classmethod
    def show(cls):
        print(cls.__name__)
s = Point08_Student()
s.show()  # OUTPUT: Point08_Student

# POINT 09 - CLASS CALL VS OBJECT CALL
# Both calls pass the same class to cls.
class Point09_Student:
    @classmethod
    def show(cls):
        print(cls.__name__)
Point09_Student.show()  # OUTPUT: Point09_Student
Point09_Student().show()  # OUTPUT: Point09_Student

# POINT 10 - CLASS METHOD + CLASS VARIABLE
# Class method is useful for reading class-level data.
class Point10_Employee:
    company = "Google"
    @classmethod
    def show_company(cls):
        print(cls.company)
Point10_Employee.show_company()  # OUTPUT: Google

# POINT 11 - MODIFY CLASS VARIABLE
# Class method can modify class-level data using cls.
class Point11_Employee:
    company = "Google"
    @classmethod
    def change_company(cls, company):
        cls.company = company
print(Point11_Employee.company)  # OUTPUT: Google
Point11_Employee.change_company("Microsoft")
print(Point11_Employee.company)  # OUTPUT: Microsoft

# POINT 12 - WHY CLASS METHOD INSTEAD OF INSTANCE METHOD?
# Company belongs to the class, so object creation is unnecessary.
# classmethod makes the intention clear: operate on the CLASS.
class Point12_Employee:
    company = "Google"
    @classmethod
    def change_company(cls, company):
        cls.company = company
Point12_Employee.change_company("Microsoft")
print(Point12_Employee.company)  # OUTPUT: Microsoft

# POINT 13 - INSTANCE METHOD VS CLASS METHOD
# Instance method -> object-specific data | Class method -> class data
class Point13_Student:
    college = "GCET"
    def __init__(self, name):
        self.name = name
    def show_student(self):
        print("Student:", self.name)
    @classmethod
    def show_college(cls):
        print("College:", cls.college)
s = Point13_Student("Harshit")
s.show_student()                  # OUTPUT: Student: Harshit
Point13_Student.show_college()    # OUTPUT: College: GCET

# POINT 14 - STATIC METHOD
# Static method receives neither self nor cls.
# Use it when logic needs neither object nor class data.
class Point14_Student:
    @staticmethod
    def is_adult(age):
        return age >= 18
print(Point14_Student.is_adult(22))  # OUTPUT: True

# POINT 15 - ALL THREE METHODS TOGETHER
# Instance -> self | Class -> cls | Static -> nothing
class Point15_Student:
    college = "GCET"
    def __init__(self, name):
        self.name = name
    def show_student(self):
        print(self.name)
    @classmethod
    def show_college(cls):
        print(cls.college)
    @staticmethod
    def is_adult(age):
        return age >= 18
s = Point15_Student("Harshit")
s.show_student()                     # OUTPUT: Harshit
Point15_Student.show_college()       # OUTPUT: GCET
print(Point15_Student.is_adult(22))   # OUTPUT: True

# POINT 16 - WHAT CAN INSTANCE METHOD ACCESS?
# Instance method has self, so it can access instance + class data.
class Point16_Student:
    college = "GCET"
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name, self.college)
Point16_Student("Harshit").show()  # OUTPUT: Harshit GCET

# POINT 17 - WHAT CAN CLASS METHOD ACCESS?
# Class method has cls, so it can directly access class-level data.
class Point17_Student:
    college = "GCET"
    @classmethod
    def show(cls):
        print(cls.college)
Point17_Student.show()  # OUTPUT: GCET

# POINT 18 - CLASS METHOD CANNOT DIRECTLY USE INSTANCE DATA
# cls represents the class, not a particular object.
# Therefore instance attributes like self.name are unavailable.
class Point18_Student:
    def __init__(self, name):
        self.name = name
    @classmethod
    def show(cls):
        # print(cls.name)  # ERROR: name belongs to object, not class
        print(cls.__name__)
Point18_Student.show()  # OUTPUT: Point18_Student

# POINT 19 - STATIC METHOD HAS NO self / cls
# It behaves like a normal function placed inside a class.
class Point19_Calculator:
    @staticmethod
    def add(a, b):
        return a + b
print(Point19_Calculator.add(10, 20))  # OUTPUT: 30


# ================================================================
# POINT 20 - WHEN TO USE STATIC METHOD?
# ================================================================
# Use for independent utility logic: validation, calculation, etc.

class Point20_Utility:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(Point20_Utility.is_even(10))  # OUTPUT: True


# ================================================================
# POINT 21 - CLASS METHOD WITH PARAMETERS
# ================================================================
# cls is automatic; other parameters are supplied by us.

class Point21_Student:
    college = "GCET"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

Point21_Student.change_college("IIT Delhi")
print(Point21_Student.college)  # OUTPUT: IIT Delhi


# ================================================================
# POINT 22 - MULTIPLE PARAMETERS
# ================================================================

class Point22_Student:
    college = "GCET"
    city = "Greater Noida"

    @classmethod
    def update(cls, college, city):
        cls.college = college
        cls.city = city

Point22_Student.update("IIT Delhi", "Delhi")
print(Point22_Student.college, Point22_Student.city)
# OUTPUT: IIT Delhi Delhi


# ================================================================
# POINT 23 - CLASS METHOD AS ALTERNATE CONSTRUCTOR
# ================================================================
# One of the most important uses of classmethod.
# It provides another way to create an object.

class Point23_Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

s = Point23_Student.from_string("Harshit,22")
print(s.name, s.age)  # OUTPUT: Harshit 22


# ================================================================
# POINT 24 - WHY "ALTERNATE CONSTRUCTOR"?
# ================================================================
# Normal: Student("Harshit", 22)
# Alternate: Student.from_string("Harshit,22")
# Both create a Student object.

class Point24_User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_email(cls, email):
        name = email.split("@")[0]
        return cls(name, email)

u = Point24_User.from_email("harshit@gmail.com")
print(u.name, u.email)  # OUTPUT: harshit harshit@gmail.com


# ================================================================
# POINT 25 - WHY cls(...) INSTEAD OF CLASSNAME(...)?
# ================================================================
# cls means CURRENT CLASS, so it works naturally with inheritance.

class Point25_Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)

s = Point25_Student.create("Harshit")
print(type(s).__name__)  # OUTPUT: Point25_Student


# ================================================================
# POINT 26 - CLASS METHOD + INHERITANCE
# ================================================================
# Calling through child class makes cls = child class.

class Point26_Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)

class Point26_CollegeStudent(Point26_Student):
    pass

s = Point26_CollegeStudent.create("Harshit")
print(type(s).__name__)  # OUTPUT: Point26_CollegeStudent


# ================================================================
# POINT 27 - HARD-CODED CLASS VS cls
# ================================================================
# cls(name) is flexible; Student(name) is hard-coded.

class Point27_Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)

class Point27_Child(Point27_Student):
    pass

s = Point27_Child.create("Rahul")
print(type(s).__name__)  # OUTPUT: Point27_Child


# ================================================================
# POINT 28 - CLASS METHOD CREATES OBJECT
# ================================================================
# Flow: classmethod -> cls(...) -> object creation -> __init__()

class Point28_Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, data):
        name, price = data.split(",")
        return cls(name, float(price))

p = Point28_Product.from_string("Laptop,75000")
print(p.name, p.price)  # OUTPUT: Laptop 75000.0


# ================================================================
# POINT 29 - CLASS METHOD VS CONSTRUCTOR
# ================================================================
# __init__ -> initializes object
# classmethod -> class operation / alternate way to create object

class Point29_Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)

s = Point29_Student.create("Harshit")
print(s.name)  # OUTPUT: Harshit


# ================================================================
# POINT 30 - CLASS METHOD IS NOT CONSTRUCTOR
# ================================================================
# Class method can CALL constructor, but they are different things.

class Point30_Student:
    def __init__(self, name):
        print("Constructor")
        self.name = name

    @classmethod
    def create(cls, name):
        print("Class Method")
        return cls(name)

s = Point30_Student.create("Harshit")
# OUTPUT:
# Class Method
# Constructor


# ================================================================
# POINT 31 - CLASS METHOD + CLASS VARIABLES
# ================================================================

class Point31_Company:
    company = "Google"
    employees = 1000

    @classmethod
    def show_info(cls):
        print(cls.company, cls.employees)

Point31_Company.show_info()  # OUTPUT: Google 1000


# ================================================================
# POINT 32 - ADD CLASS VARIABLE USING CLASS METHOD
# ================================================================

class Point32_Company:
    @classmethod
    def add_location(cls, location):
        cls.location = location

Point32_Company.add_location("Delhi")
print(Point32_Company.location)  # OUTPUT: Delhi


# ================================================================
# POINT 33 - CLASS METHOD CHANGES SHARED CLASS DATA
# ================================================================

class Point33_Student:
    college = "GCET"

s1 = Point33_Student()
s2 = Point33_Student()

Point33_Student.college = "IIT Delhi"

print(s1.college)  # OUTPUT: IIT Delhi
print(s2.college)  # OUTPUT: IIT Delhi


# ================================================================
# POINT 34 - INSTANCE DATA VS CLASS DATA
# ================================================================

class Point34_Student:
    college = "GCET"

    def __init__(self, name):
        self.name = name

s1 = Point34_Student("Harshit")
s2 = Point34_Student("Rahul")

s1.name = "Aman"
Point34_Student.college = "IIT Delhi"

print(s1.name, s2.name)  # OUTPUT: Aman Rahul
print(s1.college, s2.college)  # OUTPUT: IIT Delhi IIT Delhi


# ================================================================
# POINT 35 - INSTANCE VARIABLE IS OBJECT-SPECIFIC
# ================================================================

class Point35_Student:
    def __init__(self, name):
        self.name = name

s1 = Point35_Student("Harshit")
s2 = Point35_Student("Rahul")

s1.name = "Aman"

print(s1.name)  # OUTPUT: Aman
print(s2.name)  # OUTPUT: Rahul


# ================================================================
# POINT 36 - CLASS VARIABLE IS SHARED
# ================================================================

class Point36_Student:
    college = "GCET"

s1 = Point36_Student()
s2 = Point36_Student()

print(s1.college, s2.college)  # OUTPUT: GCET GCET

Point36_Student.college = "IIT Delhi"

print(s1.college, s2.college)  # OUTPUT: IIT Delhi IIT Delhi


# ================================================================
# POINT 37 - ALTERNATE CONSTRUCTOR FROM DICTIONARY
# ================================================================
# Very useful when data comes from API / JSON / database.

class Point37_User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["email"])

data = {"name": "Harshit", "age": 22, "email": "harshit@gmail.com"}

u = Point37_User.from_dict(data)
print(u.name, u.age, u.email)
# OUTPUT: Harshit 22 harshit@gmail.com


# ================================================================
# POINT 38 - REAL-WORLD AI/BACKEND EXAMPLE
# ================================================================
# API response -> classmethod -> object.

class Point38_AIUser:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    @classmethod
    def from_api_response(cls, data):
        return cls(data["name"], data["email"], data["role"])

data = {
    "name": "Harshit",
    "email": "harshit@gmail.com",
    "role": "AI Engineer"
}

u = Point38_AIUser.from_api_response(data)
print(u.name, u.role)  # OUTPUT: Harshit AI Engineer


# ================================================================
# POINT 39 - STATIC METHOD VS CLASS METHOD
# ================================================================
# Static -> doesn't need class/object
# Class   -> needs class information

class Point39_Student:
    college = "GCET"

    @staticmethod
    def is_valid_age(age):
        return age >= 18

    @classmethod
    def show_college(cls):
        return cls.college

print(Point39_Student.is_valid_age(22))  # OUTPUT: True
print(Point39_Student.show_college())    # OUTPUT: GCET


# ================================================================
# POINT 40 - STATIC METHOD CAN ACCESS CLASS EXPLICITLY
# ================================================================
# Static method doesn't receive cls automatically.
# But class name can be explicitly used.

class Point40_Student:
    college = "GCET"

    @staticmethod
    def show_college():
        print(Point40_Student.college)

Point40_Student.show_college()  # OUTPUT: GCET


# ================================================================
# POINT 41 - "cls" IS A CONVENTION
# ================================================================
# You can technically use another name, but "cls" is standard.

class Point41_Student:
    college = "GCET"

    @classmethod
    def show(my_class):
        print(my_class.college)

Point41_Student.show()  # OUTPUT: GCET

# ================================================================
# POINT 42 - METHOD CALLS: CLASS vs OBJECT + VARIABLE ACCESS
# ================================================================

class CompleteStudent:
    college = "GCET"  # CLASS VARIABLE
    def __init__(self, name, age):
        self.name = name  # INSTANCE VARIABLES
        self.age = age
    def show_student(self):  # INSTANCE METHOD
        print(f"Instance: {self.name}, {self.age}, {self.college}")
    @classmethod
    def show_college(cls):  # CLASS METHOD
        print(f"Class Method: {cls.college}")
    @staticmethod
    def is_adult(age):  # STATIC METHOD
        return age >= 18

# CREATE OBJECT
s = CompleteStudent("Harshit", 22)

# ================================================================
# INSTANCE METHOD CALLS
# ================================================================
# Via OBJECT -> WORKS (self = s)
s.show_student()  # OUTPUT: Instance: Harshit, 22, GCET

# Via CLASS + OBJECT -> WORKS (must manually pass object)
CompleteStudent.show_student(s)  # OUTPUT: Instance: Harshit, 22, GCET

# Via CLASS ONLY -> ERROR: missing 1 required positional argument 'self'
# CompleteStudent.show_student()  # WOULD ERROR

# ================================================================
# CLASS METHOD CALLS
# ================================================================
# Via CLASS -> WORKS (cls = CompleteStudent)
CompleteStudent.show_college()  # OUTPUT: Class Method: GCET

# Via OBJECT -> WORKS (cls still = CompleteStudent, NOT s)
s.show_college()  # OUTPUT: Class Method: GCET

# ================================================================
# STATIC METHOD CALLS
# ================================================================
# Via CLASS -> WORKS (no self/cls needed)
print(CompleteStudent.is_adult(22))  # OUTPUT: True

# Via OBJECT -> WORKS (no self/cls needed)
print(s.is_adult(22))  # OUTPUT: True

# ================================================================
# INSTANCE METHOD: ACCESS CLASS VARIABLE
# ================================================================
class TestAccess:
    college = "GCET"
    def __init__(self, name):
        self.name = name
    def show_all(self):
        print(self.college)  # Can access via self
TestAccess("Harshit").show_all()  # OUTPUT: GCET

# ================================================================
# CLASS METHOD: ACCESS CLASS VARIABLE ✓
# ================================================================
class TestClass:
    college = "GCET"
    @classmethod
    def show(cls):
        print(cls.college)  # Direct access via cls
TestClass.show()  # OUTPUT: GCET

# ================================================================
# CLASS METHOD: TRY INSTANCE VARIABLE -> ERROR
# ================================================================
class TestError:
    def __init__(self, name):
        self.name = name
    @classmethod
    def show(cls):
        # print(cls.name)  # ERROR: type object has no attribute 'name'
        print(cls.__name__)  # Works: shows class name
TestError.show()  # OUTPUT: TestError

# ================================================================
# STATIC METHOD: NEEDS EXPLICIT CLASS NAME
# ================================================================
class TestStatic:
    college = "GCET"
    @staticmethod
    def show():
        print(TestStatic.college)  # Must use class name explicitly
TestStatic.show()  # OUTPUT: GCET

# ================================================================
# MODIFY CLASS VARIABLE
# ================================================================
class Modify:
    college = "GCET"
    @classmethod
    def change(cls, new_college):
        cls.college = new_college

s1 = Modify()
s2 = Modify()
print(s1.college, s2.college)  # OUTPUT: GCET GCET
Modify.change("IIT Delhi")  # Change via classmethod
print(s1.college, s2.college)  # OUTPUT: IIT Delhi IIT Delhi (both see change)

# ================================================================
# MODIFY INSTANCE VARIABLE
# ================================================================
class ModifyInstance:
    def __init__(self, name):
        self.name = name

s1 = ModifyInstance("Harshit")
s2 = ModifyInstance("Rahul")
s1.name = "Aman"  # Change only s1
print(s1.name, s2.name)  # OUTPUT: Aman Rahul (only s1 changed)




# ================================================================
# POINT 42 - MULTIPLE CLASS METHODS
# ================================================================

class Point42_Student:
    college = "GCET"

    @classmethod
    def show(cls):
        print(cls.college)

    @classmethod
    def change(cls, college):
        cls.college = college

Point42_Student.show()             # OUTPUT: GCET
Point42_Student.change("IIT Delhi")
Point42_Student.show()             # OUTPUT: IIT Delhi


# ================================================================
# POINT 43 - CLASS METHOD + INHERITANCE + CLASS VARIABLE
# ================================================================

class Point43_Animal:
    species = "Animal"

    @classmethod
    def show_species(cls):
        print(cls.species)

class Point43_Dog(Point43_Animal):
    species = "Dog"

Point43_Animal.show_species()  # OUTPUT: Animal
Point43_Dog.show_species()     # OUTPUT: Dog


# ================================================================
# POINT 44 - WHY cls IS POWERFUL
# ================================================================
# cls automatically points to the class through which method is called.

class Point44_Payment:
    currency = "INR"

    @classmethod
    def show_currency(cls):
        print(cls.currency)

class Point44_USPayment(Point44_Payment):
    currency = "USD"

Point44_Payment.show_currency()    # OUTPUT: INR
Point44_USPayment.show_currency()  # OUTPUT: USD


# ================================================================
# POINT 45 - @classmethod DECORATOR
# ================================================================
# Recommended syntax for defining a class method.

class Point45_Demo:
    @classmethod
    def show(cls):
        print("Hello")

Point45_Demo.show()  # OUTPUT: Hello


# ================================================================
# POINT 46 - UNDERLYING CLASSMETHOD FORM
# ================================================================
# @classmethod is the clean/recommended syntax.

class Point46_Demo:
    def show(cls):
        print("Hello")

    show = classmethod(show)

Point46_Demo.show()  # OUTPUT: Hello


# ================================================================
# POINT 47 - COMPLETE METHOD COMPARISON
# ================================================================

class Point47_Student:
    college = "GCET"

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print("Instance:", self.name)

    @classmethod
    def class_method(cls):
        print("Class:", cls.__name__)

    @staticmethod
    def static_method():
        print("Static")

s = Point47_Student("Harshit")

s.instance_method()                    # OUTPUT: Instance: Harshit
Point47_Student.class_method()         # OUTPUT: Class: Point47_Student
Point47_Student.static_method()        # OUTPUT: Static


# ================================================================
# POINT 48 - CONSTRUCTOR + INSTANCE + CLASS + STATIC
# ================================================================

class Point48_Student:
    college = "GCET"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_student(self):
        print(self.name, self.age)

    @classmethod
    def show_college(cls):
        print(cls.college)

    @classmethod
    def change_college(cls, college):
        cls.college = college

    @staticmethod
    def is_adult(age):
        return age >= 18

s = Point48_Student("Harshit", 22)

s.show_student()                       # OUTPUT: Harshit 22
Point48_Student.show_college()        # OUTPUT: GCET
Point48_Student.change_college("IIT")
Point48_Student.show_college()        # OUTPUT: IIT
print(Point48_Student.is_adult(22))    # OUTPUT: True


# ================================================================
# POINT 49 - ALTERNATE CONSTRUCTOR: COMPLETE EXAMPLE
# ================================================================

class Point49_Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")
        return cls(name, int(salary))

e1 = Point49_Employee("Harshit", 50000)
e2 = Point49_Employee.from_string("Rahul,60000")

print(e1.name, e1.salary)  # OUTPUT: Harshit 50000
print(e2.name, e2.salary)  # OUTPUT: Rahul 60000


# ================================================================
# POINT 50 - JAVA: INSTANCE METHOD
# ================================================================
# Python self is conceptually similar to Java's this.

# PYTHON:
#
# class Student:
#     def show(self):
#         print(self.name)
#
# JAVA:
#
# class Student {
#     void show() {
#         System.out.println(this.name);
#     }
# }


# ================================================================
# POINT 51 - JAVA: STATIC METHOD
# ================================================================
# Python @staticmethod is conceptually close to Java static.

class Point51_Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Point51_Calculator.add(10, 20))  # OUTPUT: 30

# JAVA:
#
# static int add(int a, int b) {
#     return a + b;
# }
#
# Calculator.add(10, 20);


# ================================================================
# POINT 52 - JAVA: CLASS METHOD EQUIVALENT
# ================================================================
# Java has NO exact equivalent of Python's @classmethod.
# Closest practical pattern is a static factory method.
#
# Python:
#
# @classmethod
# def from_string(cls, data):
#     return cls(...)
#
# Java:
#
# static Student fromString(String data) {
#     return new Student(...);
# }


# ================================================================
# POINT 53 - PYTHON CLASSMETHOD vs JAVA FACTORY
# ================================================================

class Point53_Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, data):
        return cls(data)

s = Point53_Student.from_string("Harshit")
print(s.name)  # OUTPUT: Harshit

# JAVA:
#
# static Student fromString(String data) {
#     return new Student(data);
# }


# ================================================================
# POINT 54 - BIGGEST PYTHON vs JAVA DIFFERENCE
# ================================================================
# Python @classmethod receives actual class as cls.
# Java static method does NOT receive class as an implicit parameter.
#
# Python:
#
# CollegeStudent.create()
#        ↓
# cls = CollegeStudent
#
# Java:
#
# static Student create()
#        ↓
# No implicit "class object" parameter.


# ================================================================
# POINT 55 - WHEN TO USE WHAT?
# ================================================================
#
# OBJECT DATA needed?
#     -> INSTANCE METHOD
#        def method(self):
#
# CLASS DATA / CLASS operation needed?
#     -> CLASS METHOD
#        @classmethod
#        def method(cls):
#
# NEITHER object nor class needed?
#     -> STATIC METHOD
#        @staticmethod
#        def method():
#
# OBJECT INITIALIZATION?
#     -> CONSTRUCTOR
#        def __init__(self, ...):
#
# ================================================================


# ================================================================
# POINT 56 - FINAL MASTER EXAMPLE
# ================================================================
# self -> object | cls -> class | static -> nothing
# __init__ -> initialize object
# @classmethod -> class operation / alternate constructor

class Student:
    college = "GCET"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_student(self):
        print(self.name, self.age)

    @classmethod
    def show_college(cls):
        print(cls.college)

    @classmethod
    def change_college(cls, college):
        cls.college = college

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

    @staticmethod
    def is_adult(age):
        return age >= 18


# Normal constructor
s1 = Student("Harshit", 22)
s1.show_student()                     # OUTPUT: Harshit 22

# Class method
Student.show_college()                # OUTPUT: GCET

# Modify class data
Student.change_college("IIT Delhi")
Student.show_college()                # OUTPUT: IIT Delhi

# Alternate constructor
s2 = Student.from_string("Rahul,21")
print(s2.name, s2.age)                # OUTPUT: Rahul 21

# Static method
print(Student.is_adult(22))            # OUTPUT: True

