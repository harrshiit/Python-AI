# ============================================================
# 6. TYPES OF INHERITANCE  Python supports different types of inheritance:
# 1. Single Inheritance 2. Multilevel Inheritance  3. Multiple Inheritance 4. Hierarchical Inheritance
# 5. Hybrid Inheritance
# Java and Python both support inheritance,but their syntax and some inheritance rules are different.

# 1 SINGLE INHERITANCE   When ONE child class inherits from ONE parent class, One Parent → One Child
class Employee:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)

class Developer(Employee):# Developer inherits from Employee
   pass
developer = Developer("Harshit")
developer.display_name()          # Harshit
# JAVA
# class Employee { 
#      String name;
#     Employee(String name) {
#         this.name = name;
#     }
#    void displayName() {
#         System.out.println(name);
#     }
# }
# class Developer extends Employee {
#
#     Developer(String name) {
#         super(name);
#     }
# }
# Developer developer = new Developer("Harshit");
# developer.displayName();        // Harshit



# 2. MULTILEVEL INHERITANCE
# When a class inherits from another child class, forming a chain,
# it is called MULTILEVEL INHERITANCE.
# Example: User → Employee → Developer

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(self.username, "logged in successfully.")

class Employee(User):
    def show_employee_info(self):
        print("Employee:", self.username)
        print("Email:", self.email)

class Developer(Employee):
    def write_code(self):
        print(self.username, "is writing code.")

developer = Developer("Harshit", "harshit@gmail.com")

developer.login()                 # Harshit logged in successfully.
developer.show_employee_info()   # Employee: Harshit
                                  # Email: harshit@gmail.com
developer.write_code()            # Harshit is writing code.


# JAVA COMPARISON
#
# class User {
#     String username;
#     String email;
#
#     User(String username, String email) {
#         this.username = username;
#         this.email = email;
#     }
#
#     void login() {
#         System.out.println(username + " logged in successfully.");
#     }
# }
#
# class Employee extends User {
#
#     Employee(String username, String email) {
#         super(username, email);
#     }
#
#     void showEmployeeInfo() {
#         System.out.println("Employee: " + username);
#         System.out.println("Email: " + email);
#     }
# }
#
# class Developer extends Employee {
#
#     Developer(String username, String email) {
#         super(username, email);
#     }
#
#     void writeCode() {
#         System.out.println(username + " is writing code.");
#     }
# }
#
# Developer developer = new Developer("Harshit", "harshit@gmail.com");
#
# developer.login();              // Harshit logged in successfully.
# developer.showEmployeeInfo();   // Employee: Harshit
#                                 // Email: harshit@gmail.com
# developer.writeCode();          // Harshit is writing code.







# 3. HIERARCHICAL INHERITANCE
# When multiple child classes inherit from the same parent class,
# it is called HIERARCHICAL INHERITANCE.
# Example: Employee → Developer, Designer# here Both Developer and Designer inherit the common
# attributes and methods from Employee.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(self.name, self.salary)


class Developer(Employee):
    def write_code(self):
        print(self.name, "is writing code.")


class Designer(Employee):
    def design_ui(self):
        print(self.name, "is designing UI.")


developer = Developer("Harshit", 60000)
designer = Designer("Rahul", 50000)

developer.show_info()       # Harshit 60000
developer.write_code()      # Harshit is writing code.

designer.show_info()        # Rahul 50000
designer.design_ui()        # Rahul is designing UI.
# JAVA COMPARISON
#
# class Employee {
#     String name;
#     double salary;
#
#     Employee(String name, double salary) {
#         this.name = name;
#         this.salary = salary;
#     }
#
#     void showInfo() {
#         System.out.println(name + " " + salary);
#     }
# }
#
# class Developer extends Employee {
#     Developer(String name, double salary) {
#         super(name, salary);
#     }
#
#     void writeCode() {
#         System.out.println(name + " is writing code.");
#     }
# }
#
# class Designer extends Employee {
#     Designer(String name, double salary) {
#         super(name, salary);
#     }
#
#     void designUI() {
#         System.out.println(name + " is designing UI.");
#     }
# }
#
# Developer developer = new Developer("Harshit", 60000);
# Designer designer = new Designer("Rahul", 50000);
#
# developer.showInfo();       // Harshit 60000
# developer.writeCode();      // Harshit is writing code.
#
# designer.showInfo();        // Rahul 50000
# designer.designUI();       // Rahul is designing UI.\
    
# IMPORTANT: WHY DO WE NEED super()?
# If the child class does NOT define its own __init__(),
# Python can use the inherited parent __init__() automatically.
# Example:
#
# class Developer(Employee):
#     pass
#developer = Developer("Harshit", 60000)
#Here Employee.__init__() is inherited and used.
#But if the child defines its OWN __init__(),
# the parent __init__() is NOT automatically called.
#
# class Developer(Employee):
#     def __init__(self, name, salary, language):
#         self.language = language
#Now Employee.__init__() will not run automatically.
#So we use:
#
#     super().__init__(name, salary)
# to explicitly call the parent constructor. as 
# class Developer(Employee):
#     def __init__(self, name, salary, language):
#         super().__init__(name, salary)  # Call the parent constructor
#         self.language = language
# ============================================================
# JAVA COMPARISON
# ============================================================
# Java also automatically invokes the parent constructor when a child object is created, but implicitly it calls
# the parent's NO-ARGUMENT constructor using super().
#If the parent has only a parameterized constructor,
# the child must explicitly call it:
# for example:
# class Employee {
#     Employee() {
#         System.out.println("Employee constructor");
#     }
# }

# class Developer extends Employee {
#     // No constructor
# }

# Developer d = new Developer();
# // Employee() automatically called
# but if Employee has only a parameterized constructor: it will not be called automatically, like in Python,
# so we need to explicitly call it using super() in the child constructor.
# class developer extends Employee {
#     Developer(String name, double salary) {
#         super(name, salary);
#     }
# }







# 4. MULTIPLE INHERITANCE When one child class inherits from multiple parent classes,
# it is called MULTIPLE INHERITANCE.Example: SmartPhone → Camera + Phone
class Camera:
    def take_photo(self):
        print("Taking a photo.")
class Phone:
    def make_call(self):
        print("Making a call.")
class SmartPhone(Camera, Phone):
    pass


phone = SmartPhone()
phone.take_photo()       # Taking a photo.
phone.make_call()        # Making a call.
# Camera       Phone
#    \           /
#     \         /
#      ↓       ↓
#      SmartPhone
# JAVA COMPARISON
#
# Java does NOT support multiple inheritance
# through classes. all becuse  suppose 
# class Animal {
# void sound() {
#     System.out.println("Animal sound");
# }
# class Dog extends Animal {
#     void sound() {
#         System.out.println("Dog sound");
#     }
# }

# class Cat extends Animal {
#     void sound() {
#         System.out.println("Cat sound");
#     }
# }
# # now if  java allows multiple inheritance through classes, then if we create a class that inherits from both Dog and Cat,
# class Puppy extends Dog, Cat {
# Puppy p = new Puppy();
# p.sound(); // ❌ Ambiguity: Which sound() method should be called? Dog's or Cat's?`
#           Animal
#          /      \
#         Dog     Cat
#          \      /
#           Puppy
# this is called the "Diamond Problem" in multiple inheritance in java 
# }
# But in  Python this problem is solved by the Method Resolution Order (MRO) which determines the order
# in which classes are searched when looking for a method.  for example:
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Dog sound")
class Cat(Animal):
    def sound(self):
        print("Cat sound")
class Puppy(Dog, Cat):
    pass

p = Puppy()
p.sound()       # Dog sound
# here the MRO is Puppy → Dog → Cat → Animal, so Dog's sound() method is called first.
#means if sound method is not found in Puppy, it will look in Dog, then Cat, and finally Animal.
# So you don't need to directly write Animal in Puppy. Python knows about it because
# Animal is an ancestor of both Dog and Cat.

# Note : Short answer
# Java does NOT solve multiple inheritance of classes using interfaces.Instead:
# Java does not allow multiple inheritance of classes, but it provides interfaces as a way 
# to achieve multiple inheritance of type/behavior (multiple contracts).
# So in an interview, say:
# “Java avoids multiple inheritance of classes because of ambiguity such as the Diamond Problem.
# Instead, Java allows a class to implement multiple interfaces, which provides a controlled form of multiple inheritance.”
# for example:Suppose we want a SmartPhone to have both Camera and Phone capabilities.
# interface Camera {
#     void takePhoto();
# }

# interface Phone {
#     void makeCall();
# }

# class SmartPhone implements Camera, Phone {

#     public void takePhoto() {
#         System.out.println("Taking photo");
#     }

#     public void makeCall() {
#         System.out.println("Making call");
#     }
# }
    

# let suppose for  Conflicting default methods
# Java requires the class to resolve the conflict for example:
#     interface Dog {
#     default void sound() {
#         System.out.println("Dog");
#     }
# }

# interface Cat {
#     default void sound() {
#         System.out.println("Cat");
#     }
# }

# class Puppy implements Dog, Cat {

#     public void sound() {
#         Dog.super.sound();    // resolve conflict
#     }
# }
# note:ava uses interfaces to provide multiple contracts/capabilities without allowing 
# multiple class inheritance. If multiple interfaces contain conflicting default methods,
# the implementing class must explicitly resolve the conflict.
# And one more important point: Java's interface mechanism isn't merely a workaround for 
# the Diamond Problem. Interfaces are a fundamental design mechanism for abstraction, loose coupling,
# and polymorphism—even when there is no diamond or conflict at all.










# 5. HYBRID INHERITANCE  When two or more types of inheritance are combined,
# it is called HYBRID INHERITANCE.mExample: Hierarchical + Multiple Inheritance
class Employee:
    def show_employee(self):
        print("Employee")
class Developer(Employee):
    def write_code(self):
        print("Writing code")
class Designer(Employee):
    def design_ui(self):
        print("Designing UI")
# Multiple inheritance:
# FullStackDeveloper inherits from Developer and Designer
class FullStackDeveloper(Developer, Designer):
    def build_application(self):
        print("Building full-stack application")
developer = FullStackDeveloper()
developer.show_employee()        # Employee
developer.write_code()           # Writing code
developer.design_ui()            # Designing UI
developer.build_application()    # Building full-stack application
#             Employee
#             /      \
#            ↓        ↓
#       Developer   Designer
#            \        /
#             ↓      ↓
#       FullStackDeveloper
#Employee → Developer / Designer = Hierarchical Inheritance
#Developer + Designer → FullStackDeveloper = Multiple Inheritance

# JAVA COMPARISON
# Java does NOT support multiple inheritance of classes.
#Therefore this is NOT allowed:
#class FullStackDeveloper extends Developer, Designer { }
# Java can achieve a similar design using interfaces:
#
# class FullStackDeveloper extends Employee
#         implements DeveloperFeatures, DesignerFeatures {
# }