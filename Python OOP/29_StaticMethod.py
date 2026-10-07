#Basic syntax of static method in python
class Calculator:
   
   @staticmethod# this is decorator which is used to define static method thereis no keyword static in python like java or c++
    def add(a, b):
        return a + b
   
    result = Calculator.add(10, 20)#note we dont need any object to call static method we can call it directly by class name
         def add(a, b): 


    result = Calculator.add(10, 20) # note we dont need any object to call static method we can call it directly by class name
    print(result) # output: 30
#Need of static method in python
class calculator:
    def display(self): # for normal instance method we neeed to pass slef as argument or first parameter of method is self
        print("This is a display method")
    def display2()  # if we dont pass self it will give error because it is not a static method and we are not passing self as first parameter 
        print("This is a display2 method") 
         def display2(self):  # if we dont pass self it will give error because it is not a static method and we are not passing self as first parameter 
        return a + b
    
    print(calculator.display())  # Python internally does: calculator.display(obj)
        # Here 'obj' becomes 'self'.If NO object is created and we do:  Python has nothing to pass as 'self'. Therefore -> ERROR
         # print(calculator.display())  # Python internally does: calculator.display(obj)
# Python does not automatically pass an object, because we are calling it through the CLASS.So there is no missing 'self' in this particular call.
# However, this is still NOT formally a static method. To explicitly say:"This method does not need an object",
 # we should use @staticmethod.  othewise it will give error
    print(calculator.add(10, 20)) # this will work fine becuse we are access  it  from class name 
    # suppupse we perform some  function through  object 
    obj = calculator()
    print(obj.display()) # this will work fine because we are accessing it through object and self is passed automatically
    print(obj.display2()) # this will give error because we are accessing it through object and self is not passed automatically
         # print(obj.display2()) # this will give error because we are accessing it through object and self is not passed automatically
    print(obj.add(10, 20)) # this will give error because we are accessing 
    #it through object and self is not passed automatically  because it  internally python does: obj.add(obj, 10, 20) but we are not passing self as first parameter 
    # as it is assign like  a=self b=10
    
    
    


#Declaration of static method in python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
         result = Calculator.add(10, 20) # here Python does not automatically pass an object.
     # and even when we call it through an object, Python does not automatically pass an object.
    c = Calculator()
    c.add(10, 20) # here  c.add(10,20) is equivalent to add(10, 20 ) not add(c, 10, 20)
    
    
    
    # A static method can access its own local variables and parameters,
    # but it cannot directly access instance variables (self) or class variables (cls) 
    # unless you explicitly provide a way to access them.
    class Calculator:
     company = "My Calculator"#class variable or class attribute
      #constructor of class
      def __init__(self, name):
        self.name = name # this is instance variable or instance attribute
        #instance Method 
      def instance_method(self, number):
         print(number)        # ✅ Can access its parameters
        print(self.name)        # ✅ Can access instance variable
        print(Calculator.company)        # ✅ Can access class variable
         print(self.company) #this can also be  posssible  
# class Method
     @classmethod
    def class_method(cls, number):
       print(number)        # ✅ Can access its parameters
       print(self.name)            #  error ❌ Cannot directly access instance variable
       print(cls.company)           # ✅ Can access class variable
    #Static Method 
    @staticmethod
    def static_method(number):
       print(number)        # ✅ Can access its parameters
       print(self.name)        # ❌ Cannot access instance variable
       print(cls.company)              # ❌ Cannot use cls
       print(Calculator.company)          # ✅ Can access class variable using class name
       result = number * 2            # ✅ Can create and use its own local variable
        print(result)
        
        
#python have not ability to pass object automatically to static method 
#but we can pass an object manually 
class Calculator:

    def __init__(self, brand):  # Constructor; self receives current object  Instance variable
       self.brand = brand                     
   
    def show_brand1(self):    # Instance method → self is automatically required self refers to the calling object
        print(self.brand)                      

    @staticmethod    # Makes show_brand2() a static method No self → object is NOT automatically passed
    def show_brand2():                         
        print("Static method")    #Can be called without creating an object

    @staticmethod                              
    def show_brand3(calculator):    # Manually passed object can access its instance variable
           
        print(calculator.brand)                

c1 = Calculator("Casio")                       # c1.brand = "Casio"
c2 = Calculator("Rolex")                       # c2.brand = "Rolex"

c1.show_brand1()                               # Correct → Python automatically passes c1 as self
Calculator.show_brand1(c1)                    # Also correct → manually passing object as self

 Calculator.show_brand1()                    # ❌ Error → self/object argument is missing

Calculator.show_brand2()                      # Correct → no object required
c1.show_brand2()                               # Also correct → c1 is NOT automatically passed

# STATIC METHOD WITH MANUALLY PASSED OBJECT

Calculator.show_brand3(c1)                    # Correct → c1 is manually passed to calculator
Calculator.show_brand3(c2)                    # Correct → c2 is manually passed to calculator

c1.show_brand3(c1)                             # Correct → first c1 accesses method; second c1 is argument
c2.show_brand3(c2)                             # Same idea → calculator receives c2
c1.show_brand3()                            # ❌ Error → calculator argument is missing





#Static Method Calling Another Static Method
class Calculator:

    @staticmethod
    def square(n):
        return n * n

    @staticmethod
    def cube(n):
        return n * n * n

    @staticmethod
    def display():
        print(Calculator.square(5))
        print(Calculator.cube(5))
Calculator.display()  # output is 25 and 125


#Static  Method call  normal function 
def greet():
    print("Hello")
class Test:

    @staticmethod
    def run():
        greet()
Test.run()    #Hello


#Static Methods Are Often Used for Utility Functions
class StringUtils:
    @staticmethod
    def is_palindrome(text):
        return text == text[::-1]

    @staticmethod
    def reverse(text):
        return text[::-1]

    @staticmethod
    def word_count(text):
        return len(text.split())
print(StringUtils.is_palindrome("madam"))
print(StringUtils.reverse("Python"))
print(StringUtils.word_count("Python is easy"))




#Static Method vs Instance Method
class Student:
      def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
s = Student("Harshit")  #specific object's data needs 
s.display()

#vs 
class Student:

    @staticmethod
    def calculate_grade(marks):
        if marks >= 90:
            return "A"
        return "B"
    Student.calculate_grade(95)# need not any object 
    
    


#Important: Static Method Is Not the Same as a Global Function
def calculate_interest(principal, rate):  #You could simply write:
    return principal * rate / 100
# Why put it inside a class? Because sometimes the function is conceptually related to the class.
class Account:

    @staticmethod
    def calculate_interest(principal, rate):
        return principal * rate / 100
    
    


# Static Method Can Accept *args
class Calculator:

    @staticmethod
    def add(*numbers):
        return sum(numbers)
print(Calculator.add(10, 20))
print(Calculator.add(10, 20, 30, 40))



# Static Method Can Raise Exceptions
