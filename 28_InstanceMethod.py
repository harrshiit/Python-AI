# ================================================================
# INSTANCE METHODS — PYTHON vs JAVA (FULL REVISION FILE)
# Scope: Instance methods only. Class methods / static methods = later topic.
# NOTE: Not meant to be run top-to-bottom (class names repeat on purpose,
# one focused example per concept). Read section by section.
# ================================================================


# ================================================================
# 1. WHAT IS AN INSTANCE METHOD?
# ================================================================
# An instance method works with a particular object (instance) and can
# access/modify that object's data.
# Syntax: def method_name(self): ...   self = current object.

class Student:
    def display(self):
        print("Student display method")

s1 = Student()
s1.display()

# JAVA:
# class Student { void display() { System.out.println("Student display method"); } }
# Student s1 = new Student(); s1.display();
#
# Python instance method <=> Java normal non-static instance method.
# Both are called using an object: Python s1.display() | Java s1.display()


# ================================================================
# 2. self — CURRENT OBJECT
# ================================================================
class Student:
    def display(self):
        print(self)

s1, s2 = Student(), Student()
s1.display()   # self = s1
s2.display()   # self = s2

# self refers to the current object: s1.display() -> self=s1; s2.display() -> self=s2.
# Java uses 'this' for the current object.
# Python: self (explicit first parameter) | Java: this (implicitly available).
# self is NOT a Python keyword; it is the standard naming convention and should always be used.


# ================================================================
# 3. INSTANCE VARIABLES + INSTANCE METHODS
# ================================================================
class Student:
    def __init__(self, name, age):
        self.name, self.age = name, age
    def display(self):
        print("Name:", self.name); print("Age:", self.age)

s1 = Student("Harshit", 22)
s1.display()

# self.name/self.age are instance variables belonging to a particular object.
# display() accesses them using self.
# JAVA:
# class Student {
#     String name; int age;
#     Student(String name,int age){ this.name=name; this.age=age; }
#     void display(){ System.out.println(this.name); System.out.println(this.age); }
# }
# Python self.name <=> Java this.name.


# ================================================================
# 4. INSTANCE METHOD WITH PARAMETERS
# ================================================================
class Calculator:
    def add(self, a, b):
        return a + b

c1 = Calculator()
result = c1.add(10, 20)
print(result)

# add() has self=current object, a=first argument, b=second argument.
# c1.add(10,20) automatically passes c1 as self.
# Conceptually: Calculator.add(c1,10,20).
# JAVA:
# class Calculator { int add(int a,int b){ return a+b; } }
# Calculator c1=new Calculator(); int result=c1.add(10,20);
# Difference: Python explicitly writes self; Java implicitly provides current object through this.


# ================================================================
# 5. INSTANCE METHOD CAN MODIFY OBJECT STATE
# ================================================================
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def display_balance(self):
        print("Balance:", self.balance)

account = BankAccount(1000)
account.deposit(500); account.display_balance()

# Instance methods can modify object state; self.balance is the current object's balance.
# JAVA:
# class BankAccount {
#     double balance;
#     BankAccount(double balance){ this.balance=balance; }
#     void deposit(double amount){ this.balance+=amount; }
#     void displayBalance(){ System.out.println(this.balance); }
# }
# Instance method + instance variable -> object's state and behavior.


# ================================================================
# 6. SAME INSTANCE METHOD — DIFFERENT OBJECTS
# ================================================================
class Student:
    def __init__(self, name, marks):
        self.name, self.marks = name, marks
    def display(self):
        print(self.name, self.marks)

s1 = Student("Harshit",90); s2 = Student("Rahul",80)
s1.display(); s2.display()

# Same display() method + different object -> different object state.
# s1.display() -> self=s1; s2.display() -> self=s2.
# JAVA:
# Student s1=new Student("Harshit",90); Student s2=new Student("Rahul",80);
# s1.display(); s2.display();  // Same OOP concept; Java uses this.


# ================================================================
# 7. INSTANCE METHOD CAN RETURN A VALUE
# ================================================================
class Rectangle:
    def __init__(self, length, width):
        self.length, self.width = length, width
    def area(self):
        return self.length * self.width

r1 = Rectangle(10,5)
print(r1.area())   # 50

# area() returns a value using the current object's instance variables.
# JAVA (FIXED — original draft was missing the constructor, which made
# r1.area() return 0 instead of 50):
# class Rectangle {
#     int length, width;
#     Rectangle(int length, int width){ this.length=length; this.width=width; }
#     int area(){ return this.length*this.width; }
# }
# Rectangle r1 = new Rectangle(10,5);
# System.out.println(r1.area());   // 50


# ================================================================
# 8. INSTANCE METHOD CAN CALL ANOTHER INSTANCE METHOD
# ================================================================
class Student:
    def calculate_percentage(self, marks):
        return marks / 5
    def display_result(self, marks):
        percentage = self.calculate_percentage(marks)
        print("Percentage:", percentage)

s1 = Student()
s1.display_result(400)

# One instance method can call another using self.
# self.calculate_percentage() means "call calculate_percentage() for this same object."
# JAVA:
# class Student {
#     double calculatePercentage(int marks){ return marks/5.0; }
#     void displayResult(int marks){
#         double percentage=this.calculatePercentage(marks);
#         System.out.println(percentage);
#     }
# }
# Python self.calculate_percentage() <=> Java this.calculatePercentage().


# ================================================================
# 9. CALLING INSTANCE METHOD THROUGH CLASS
# ================================================================
class Test:
    def display(self):
        print("Hello")

t1 = Test()
t1.display()          # Normal/recommended way
Test.display(t1)      # Technically possible

# t1.display() and Test.display(t1) are conceptually equivalent.
# Python automatically passes t1 as self; conceptually: Test.display(t1), so self=t1.
# JAVA: normally t1.display(); a non-static instance method is not normally
# called through the class in the same way Python technically allows.


# ================================================================
# 16. WHAT IF WE DON'T MENTION self?
# ================================================================

# Normal instance method:
# def display(self): ...
# When obj.display() is called, Python automatically passes the current object.
# Therefore the method needs a parameter to receive that object.

class Student:
    def display(self):
        print("Hello")

s1 = Student()
s1.display()                 # CORRECT

# Internally/approximately: Student.display(s1) -> self = s1.


# SCENARIO 1: We DON'T write self
class Student:
    def display():
        print("Hello")

s1 = Student()
# s1.display()              # ERROR:
# TypeError: Student.display() takes 0 positional arguments but 1 was given
#
# Why? s1.display() -> Python automatically passes s1 -> Student.display(s1),
# but display() has ZERO parameters, so there is nowhere to put s1.
#
# JAVA COMPARISON:
# Java does NOT require this as a parameter:
# void display(){ System.out.println("Hello"); }
# Java automatically provides the current object through 'this'.
# Python: def display(self): -> self must explicitly receive the object.


# ================================================================
# 17. WHAT IF WE WRITE ANOTHER NAME INSTEAD OF self?
# ================================================================
class Student:
    def display(x):
        print(x)

s1 = Student()
s1.display()                 # WORKS

# self is NOT a Python keyword; Python only cares that the first parameter
# receives the object. Therefore def display(x) works like def display(self).
# BUT NEVER use x, obj, abc, etc. in normal code. Always use self because
# self is the standard Python convention.


# ================================================================
# 18. WHAT IF WE WRITE TWO PARAMETERS BUT EXPECT ONE?
# ================================================================
class Student:
    def display(self, name):
        print(name)

s1 = Student()

# s1.display()               # ERROR
# Python automatically supplies self=s1, but name is also required.
# Therefore Python expects s1.display("Harshit"):
# self=s1, name="Harshit".

s1.display("Harshit")        # CORRECT

# CONCEPT: self is automatically supplied; other parameters normally
# must be supplied by us.


# ================================================================
# 19. WHAT IF WE MANUALLY PASS self?
# ================================================================
class Student:
    def display(self):
        print(self)

s1 = Student()
s1.display()                 # CORRECT

# We DON'T write s1.display(s1), because Python already passes s1 automatically.
# s1.display(s1) effectively becomes Student.display(s1, s1).
# But display() accepts only one parameter (self), so this causes TypeError.
#
# IMPORTANT:
# Normal call -> s1.display()
# NOT -> s1.display(s1)


# ================================================================
# 20. CLASS CALL — HERE WE CAN PASS THE OBJECT MANUALLY
# ================================================================
class Student:
    def display(self):
        print("Hello")

s1 = Student()
s1.display()                 # Normal call
Student.display(s1)          # Class-based call

# s1.display() -> Python automatically passes s1.
# Student.display(s1) -> WE explicitly pass s1.
# Therefore both are effectively equivalent:
# s1.display() <-> Student.display(s1)


# ================================================================
# 24. CAN AN INSTANCE METHOD INITIALIZE OBJECT DATA?
# ================================================================
class Student:
    def set_data(self, name, age):
        self.name = name
        self.age = age

s1 = Student()
s1.set_data("Harshit", 22)
print(s1.name); print(s1.age)

# YES! An instance method CAN create/initialize instance attributes.
# self.name=name and self.age=age create/assign data to the object.
# So why do we need __init__()? -> Constructor and instance method have DIFFERENT PURPOSES.


# ================================================================
# 25. CONSTRUCTOR vs INSTANCE METHOD
# ================================================================

# CONSTRUCTOR    -> Initializes an object when the object is created.
# INSTANCE METHOD -> Performs an operation/behavior on an already-created object.
#
# Python:
# __init__()           -> initializes object during creation.
# Normal instance method -> performs behavior after creation.


# ================================================================
# 26. USING CONSTRUCTOR — RECOMMENDED FOR INITIAL STATE
# ================================================================
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)

s1 = Student("Harshit", 22)
s1.display()

# __init__() is automatically called during object creation:
# Student("Harshit",22) -> __init__(self,"Harshit",22) -> object initialized immediately.
#
# JAVA:
# class Student {
#     String name; int age;
#     Student(String name,int age){ this.name=name; this.age=age; }
# }
# Student s1=new Student("Harshit",22);
#
# Java constructor and Python __init__ have a similar purpose:
# initializing object state during object creation.


# ================================================================
# 27. USING INSTANCE METHOD FOR INITIALIZATION
# ================================================================
class Student:
    def set_data(self, name, age):
        self.name = name
        self.age = age

s1 = Student()
s1.set_data("Harshit",22)
print(s1.name); print(s1.age)

# This ALSO works, but object is created first:
# Student() -> object exists -> set_data() initializes data later.
# Therefore the object exists BEFORE its important data is assigned.


# ================================================================
# 28. WHY USE CONSTRUCTOR IF INSTANCE METHOD CAN DO IT?
# ================================================================

# With:
# class Student:
#     def set_data(self,name,age):
#         self.name=name; self.age=age
#
# We can do:
# s1=Student(); s1.set_data("Harshit",22)
#
# BUT someone can also do:
# s1=Student()
# and forget set_data().
#
# Now s1 does not have name and age.
# Constructor solves this by forcing required initialization at object creation.


# ================================================================
# 29. CONSTRUCTOR ENSURES REQUIRED INITIAL STATE
# ================================================================
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)

# s1=Student()                # ERROR: TypeError - required arguments missing
s1 = Student("Harshit",22)    # CORRECT
s1.display()

# Constructor ensures every Student object starts with required data.
# This is a major reason constructors are useful.


# ================================================================
# 30. INSTANCE METHOD = CHANGE / UPDATE OBJECT AFTER CREATION
# ================================================================
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount("Harshit",1000)
account.deposit(500)
account.withdraw(200)

# Constructor -> establishes initial state.
# Instance methods -> change/update/use that state later.
#
# Object lifecycle:
# CREATE -> __init__() -> Initial state -> instance methods -> modify/use state.


# ================================================================
# 31. REAL-LIFE EXAMPLE
# ================================================================
class Car:
    # Constructor -> initial state
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    # Instance methods -> behavior/state operations
    def accelerate(self, amount):
        self.speed += amount
    def brake(self, amount):
        self.speed -= amount
    def display(self):
        print(self.brand, self.speed)

car = Car("BMW",0)
car.accelerate(50)
car.accelerate(20)
car.brake(10)
car.display()

# Constructor -> "What should this object START with?"
# Instance method -> "What should this object DO after it exists?"
#
# Constructor: brand=BMW, speed=0
# Instance methods: accelerate(), brake(), display()


# ================================================================
# 32. JAVA EQUIVALENT
# ================================================================

# PYTHON:
# class Car:
#     def __init__(self,brand,speed):
#         self.brand=brand; self.speed=speed
#     def accelerate(self,amount):
#         self.speed+=amount
# car=Car("BMW",0); car.accelerate(50)
#
# JAVA:
# class Car {
#     String brand; int speed;
#     // Constructor
#     Car(String brand,int speed){ this.brand=brand; this.speed=speed; }
#     // Instance method
#     void accelerate(int amount){ this.speed+=amount; }
# }
# Car car=new Car("BMW",0); car.accelerate(50);
#
# DIFFERENCE:
# Python constructor initialization -> __init__()
# Java constructor -> Car(...)
# Python instance method -> def accelerate(self,amount)
# Java instance method -> void accelerate(int amount)
# Both have the same basic OOP purpose.


# ================================================================
# 33. IMPORTANT DIFFERENCE — CONSTRUCTOR vs set_data()
# ================================================================

# APPROACH 1: Constructor
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Harshit",50000)

# Object is created and initialized together.
# Employee("Harshit",50000) -> generally preferred when data is REQUIRED.


# APPROACH 2: Instance method
class Employee:
    def set_data(self, name, salary):
        self.name = name
        self.salary = salary

e2 = Employee()
e2.set_data("Harshit",50000)

# Object creation and initialization happen separately:
# Employee() -> set_data()
#
# Useful when:
# - Data is not available at object creation.
# - Data needs to be changed later.
# - You intentionally want a separate setup/configuration step.


# ================================================================
# 34. INSTANCE METHOD CAN BOTH SET AND UPDATE DATA
# ================================================================
class Student:
    def __init__(self, name):
        self.name = name
    def set_name(self, name):
        self.name = name

s1 = Student("Harshit")
print(s1.name)
s1.set_name("Rahul")
print(s1.name)

# Constructor -> initial value = Harshit.
# Instance method -> updates value = Rahul.
#
# Common pattern:
# Constructor -> initial state
# Instance methods -> operations / modifications