class Student:
  def __init__(self):# here self is used to refer to the current object being created. 
      #It is a reference to the instance of the class.for example, 
      # if we create an object s of the Student class, then self will refer to s inside the __init__() method.
    print("Constructor called")
s = Student() # here __init__() is automatically invoked when the object is created.
#and print statement " constructor called" is printed on the console.

#Java Constructor:

    # class Student {

    #     Student() { self is not used in java constructor because it is automatically invoked when the object is created.
    #         System.out.println("Constructor called");
    #     }
    # }

    # Student s = new Student(); here we have to define it in  main in order 
    # to call the constructor and print statement " constructor called" is printed on the console.

#--------------------------------------Purpose----------------------------------------------------
class Student:
    name
    age 
    branch
  # Without __init__(), we could manually assign values: 
 s1= Student()
 
    s.name = "Harshit"
    s.age = 22
    s.branch = "CSE"
s2=Student()
    s2.name = "Rahul"
    s2.age = 21
    s2.branch = "ECE"

# with constructor we can initialize the object with values at the time of creation for example:
class Student:
    def __init__(self, name, age, branch):#constructor is defined with parameters name, age, and branch.
        self.name = name
        self.age = age
        self.branch = branch
s1= Student("Harshit", 22, "CSE")
s2= Student("Rahul", 21, "ECE")

#In java we can do the same thing like this: for ex
class  Student {
    String name;
    int age;
    String branch;
    Student(String name, int age, String branch) {
        this.name = name;
        this.age = age;
        this.branch = branch;
    }
    

# class Student {

#         String name;
#         int age;
#         String branch;

#         Student(String name, int age, String branch)# constructor is defined with parameters name, age, and branch.
#         #self is not used in java constructor because it is automatically invoked when the object is created. 
#         {
#             # but we use this keyword to refer to the current object being created.
#             # It is a reference to the instance of the class.
#             this.name = name;
#             this.age = age;
#             this.branch = branch;
#         }
#     }
# Student s1 = new Student("Harshit", 22, "CSE");
# Student s2 = new Student("Rahul", 21, "ECE");

# 3. WHAT IS self?


# Java:  this.name  means:name belonging to the current object.

# Python:self.name  means:name belonging to the current object.

# Unlike Java, Python requires us to explicitly write self as the
# first parameter of an instance method.Example:
#  def __init__(self, name):
#         self.name = name
#     self       -> current object
#     name       -> parameter/local variable
#     self.name  -> instance variable/attribute

#   In Java, this is automatically available inside instance methods, so we don't have to explicitly write it.
#     Student(String name) {
#         this.name = name;
#     }

#   Java this  ≈  Python self
#    and java class name = to python __init__
#    for example:
#    java constructor Student(String name){} is equivalent to python constructor def __init__(self, name)


# HOW IS __init__() CALLED AUTOMATICALLY?

class Student:

        def __init__(self):
            print("init invoked automatically")
        def display(self):
            print("hello world")
s = Student() # on object creation, __init__() is automatically invoked and print statement "init invoked automatically" is printed on the console.
s.display() # here display() method  have  to called  explicitly to print "hello world" on the console. using dot operator on the object s.
#but for  init method it autoamatically do internally s.__init__()  when we create the object s of class Student.

#  IN java, the constructor is automatically invoked when we create an object of the class. For example:
 
 
#  class Student {
#  Student() { System.out.println("Constructor invoked automatically"); }
# void display() {
#     #here we need not to write self as argument because in java it is automatically invoked when we create an object of the class.
#   System.out.println("Hello World");}
#     }
# public class Main {
#         public static void main(String[] args) {
#             Student s = new Student(); // Constructor is automatically invoked here
#             s.display(); // display() method has to be called explicitly
#              # the output will be:
#             # Constructor invoked automatically
#             # Hello World
#         }
#     }




class Student:

    def __init__(self, name):
        print("Inside __init__()")
        self.name = name
# __init__() is automatically invoked here
s = Student("Harshit")
print(s.name)  #conceptually python internally calls Student.__init__(s, "Harshit") when the object s is created.
# Output:
# Inside __init__() 
#Harshit



class Student:
     name
    def __init__(self, name):
        self.name = name


s1 = Student("Harshit")
s2 = Student("Rahul")
#internally python calls Student.__init__(s1, "Harshit") and Student.__init__(s2, "Rahul") when the objects s1 and s2 are created.

print(s1.name)  # Harshit
print(s2.name)  # Rahul

# ============================================================
# DEFAULT CONSTRUCTOR
# ============================================================
#
# WHAT HAPPENS IF WE DON'T DEFINE __init__() IN PYTHON? Python allows us to create an object even if we don't
# explicitly define __init__().
# Python provides a default constructor automatically. However, class variables like name and age are NOT
# automatically initialized for each object.



class Student:
    name 
s1 = Student() # here python defauly call internal __init__() method to create the object s1 of class Student.
# here coceptually two things happen:
# s1 = Student.__new__(Student)   # creates the object
# Student.__init__(s1)            # initializes the object
print(s1.name)   # Output: AttributeError: 'Student' object has no attribute 'name'

# But in java
 
#  class Student {
#         String name;  // instance variable also here no value provided but java still gives default value to instance variable. 
#         // which is null for String and 0 for int, etc. if no value is provided. which is not the case in python.
#         // python does not give default value to instance variable if  we  do so give an error AttributeError
#         }
#  Student s1 = new Student(); //internally java calls
#    // Student(){
#     //    this.name = null;  # java automatically gives default value to instance variable if no value is provided.
#    //     } constructor to create the object s1 of class Student.
#    
# System.out.println(s1.name); // Output: null



class Student:

    def __init__(self, name):
        self.name = name
s1 = Student("Harshit") # correct to pass argumrnt if constructor image is that
print(s1.name)
 s2 = Student() #Incorrect to not pass argument if constructor image is that becuse __init__() 
 #is defined with parameter name, so we have to pass argument while creating the object s2 of class Student.
#as it stop automatically calling __init__() with default constructor because we have defined __init__() with parameter name, so we have to pass argument while creating the object s2 of class Student.
# This causes TypeError: Student.__init__() missing 1 required positional argument: 'name'


#Same in java:
# class Student {
#     String name;
#     Student(String name) {
#         this.name = name;
#     }
# } 
# Student s1 = new Student("Harshit"); // correct
# Student s2 = new Student(); // incorrect, causes compile-time error: constructor Student in class Student cannot be applied to given types;
# //required: String; found: no arguments; reason: actual and formal argument lists differ in length

# ==================================================================
# 10. PARAMETERIZED CONSTRUCTOR
# ==================================================================
class Student:
   def __init__(self, name, age):
            self.name = name
            self.age = age
s1 = Student("Harshit", 22)
s2 = Student("Rahul", 21)
#Each object gets different values.

#In java we can do the same thing like this: for ex
#     class Student {
#         String name;
#         int age;
#   Student(String name, int age) {
#             this.name = name;
#             this.age = age;
#         }
#     }
# Student s1 = new Student("Harshit", 22);
#     Student s2 = new Student("Rahul", 21);


class Student:

    def __init__(self, name, age, branch):

        self.name = name
        self.age = age
        self.branch = branch

    def display(self):

        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Branch :", self.branch)


s1 = Student("Harshit", 22, "CSE")

s1.display()


# ==================================================================
# 12. CONSTRUCTOR WITHOUT PARAMETERS
# ==================================================================

"""
A Python __init__() can contain only self.

Example:

    def __init__(self):
        ...

This is often called a non-parameterized constructor/initializer.

Example:

    class Student:

        def __init__(self):
            self.name = "Unknown"
            self.age = 0

Java equivalent:

    class Student {

        Student() {
            this.name = "Unknown";
            this.age = 0;
        }
    }

"""


class Student:
  def __init__(self):
        self.name = "Unknown"
        self.age = 0
s = Student()
print(s.name)#It will print "Unknown" because we have defined the default value of name as "Unknown" in the constructor.
print(s.age)#It will print 0 because we have defined the default value of age as 0 in the constructor.


# ==================================================================
# 13. IMPORTANT DIFFERENCE:
#    DEFAULT CONSTRUCTOR vs NON-PARAMETERIZED CONSTRUCTOR

# 1. CLASS WITHOUT __init__
# ================================================================
class Student1: pass
s1 = Student1()
print(s1) #output: <__main__.Student1 object at 0x7f8c8c8c8c8c>
# Object is successfully created.
# JAVA:
# class Student1 {}
# Student1 s1 = new Student1();
# This also works. If you don't write ANY constructor in Java,
# Java automatically provides a no-argument constructor.
# So Student1 s1 = new Student1(); works.

# What if we try: 
print(s1.name)# ❌ Python: AttributeError — 'name' was never created.
# JAVA: System.out.println(s1.name);
# ❌ Compile-time error — 'name' was never DECLARED inside Student1.
# Java does NOT allow access to a variable that doesn't exist in the class.

s1.name = "Rahul"# Python allows this: the object initially had no 'name'; we created it later.
print(s1.name)# Output: Rahul
# JAVA: You CANNOT normally do s1.name = "Rahul";
# if 'name' was never declared inside the class.Java requires:
# class Student1 { String name; }before s1.name = "Rahul";
# IMPORTANT DIFFERENCE:
# Python: Object can get a new attribute dynamically.
# Java: Instance variables are declared as part of the class.



# ================================================================
# PARAMETERIZED __init__ WITH DEFAULT VALUES
# ================================================================
class Student4:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
# No arguments
s5 = Student4()
print(s5.name)
print(s5.age)
# Output: Unknown, 0

# Both arguments
s6 = Student4("Amit", 25)
print(s6.name)
print(s6.age)
# Output: Amit, 25

# Only name
s7 = Student4("Neha")
print(s7.name)
print(s7.age)
# Output: Neha, 0

# JAVA DIFFERENCE:
# Python directly supports default parameters:
# def __init__(self, name="Unknown", age=0):
# Java does NOT support default parameter values in constructors like this.
# Instead, Java commonly uses constructor overloading.
#
# class Student4 {
#     String name; int age;
#     Student4() { name = "Unknown"; age = 0; }
#     Student4(String name) { this.name = name; this.age = 0; }
#     Student4(String name, int age) {
#         this.name = name; this.age = age;
#     }
# }
# Now Java can do:
# Student4 s5 = new Student4();
# Student4 s6 = new Student4("Amit", 25);
# Student4 s7 = new Student4("Neha");
# This is called CONSTRUCTOR OVERLOADING.

# 9. ATTRIBUTE DOES NOT EXIST
# ================================================================
class Student6:
    def __init__(self):
        self.name = "Rahul"

s8 = Student6()
print(s8.name) # Output: Rahul
s8.name = "Amit" # we can change the value of name attribute because it was created in __init__().
print(s8.name) # Output: Amit
s8.age = 21 # we can create a new attribute age dynamically because python allows it.

# This works because __init__ created self.name = "Rahul".
# JAVA:
# class Student6 {
#     String name;
#     Student6() { name = "Rahul"; }
# }
# Student6 s8 = new Student6();
# System.out.println(s8.name); -> works.
# But System.out.println(s8.age);
# ❌ Compile-time error because 'age' was not declared in Student6.



# Python:
class PythonStudent:
    def __init__(self, name):
        self.name = name

p = PythonStudent("Rahul")
print("\n--- 9. CONSTRUCTOR RULE ---")
print(p.name)

# If we do p = PythonStudent()❌ TypeError because name is required.
#
# JAVA:
# class JavaStudent {
#     String name;
#     JavaStudent(String name) { this.name = name; }
# }
# JavaStudent s = new JavaStudent("Rahul"); -> works.
#
# BUT:
# JavaStudent s = new JavaStudent();
# ❌ Compile-time error because once you write:
# JavaStudent(String name)
# Java does NOT automatically create:
# JavaStudent()
#
# If you want both, you must explicitly write both:
# class JavaStudent {
#     String name;
#     JavaStudent() { name = "Unknown"; }
#     JavaStudent(String name) { this.name = name; }
# }
# Then BOTH work:
# JavaStudent s1 = new JavaStudent();
# JavaStudent s2 = new JavaStudent("Rahul");



