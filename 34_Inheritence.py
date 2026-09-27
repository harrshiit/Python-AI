# 1. WHY DO WE NEED INHERITANCE?
# 1. Developer 2. Designer Both employees have some common data and behavior:
# name salary display_info()  Without inheritance, we may have to write
# the same code again and again.
class Developer:
      def __init__(self, name, salary):
        self.name = name
        self.salary = salary
      def display_info(self):
        print(self.name, self.salary)


class Designer:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(self.name, self.salary)
developer = Developer("Harshit", 60000)
designer = Designer("Rahul", 50000)

developer.display_info()
designer.display_info()
# PROBLEM If we have many employee types:Developer   Designer Tester ManagerDataScientist
# we may have to repeatedly write the same common properties and methods in every class.
# This makes the code:1. Repetitive2. Harder to maintain 3. Harder to modify4. More prone to errors
       


# 2. HOW DOES INHERITANCE SOLVE THIS PROBLEM?
# Inheritance allows a child class to reuse theattributes and methods of an existing parent class.
#Common code is written only ONCE in the parent class. Child classes inherit and reuse that code.
class Employee: # parent class / base class

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(self.name, self.salary)

class Developer(Employee): # child class / derived class
    pass
class Designer(Employee):# this is also a child class / derived class
    pass

developer = Developer("Harshit", 60000)
designer = Designer("Rahul", 50000)
developer.display_info()
designer.display_info()
# No need to rewrite __init__() or display_info() inside Developer and Designer.





# ============================================================
# 5. CHILD CLASS CAN HAVE ITS OWN FEATURES
# ============================================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(self.name, self.salary)
# Developer inherits Employee and adds its own feature: programming_language
class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary) #super() is used to call the parent class's __init__()
        #method to initialize the inherited attributes name and salary.
        self.programming_language = programming_language
     def write_code(self):
        print(self.name, "is writing", self.programming_language, "code")
developer = Developer("Harshit", 60000, "Python")
print(developer.name)          # Harshit
print(developer.salary)        # 60000
developer.display_info()       # Harshit 60000
print(developer.programming_language)   # Python this  is child class specific attribute
developer.write_code() # Harshit is writing Python code


