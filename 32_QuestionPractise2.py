# <! -- EMPLOYEE MANAGEMENT & PAYROLL SYSTEM

# Design an Employee Management and Payroll System using Python OOP.

# The system should create employees with their name, employee ID,
# department, and basic salary. Each employee should be automatically registered in the company,
# and the system must maintain the total number of employees created. The company should also maintain a common 
# company-wide bonus percentage that can be changed when required. Provide functionality to display an individual 
# employee's details and calculate their final salary after applying the
# current company bonus. Also provide an independent utility to calculate tax on any given salary and 
# tax percentage without depending on any particular employee or company data. -- >
class Employee:
    # Class variable: ye poori Employee class ka common data hai
    total_employees = 0

    # Company-wide bonus: sabhi employees ke liye common bonus percentage
    company_bonus = 10

    def __init__(self, name, employee_id, department, basic_salary):
        # Instance variable: har employee ka apna name hota hai
        self.name = name

        # Instance variable: har employee ki unique ID hoti hai
        self.employee_id = employee_id

        # Instance variable: har employee ka department different ho sakta hai
        self.department = department

        # Instance variable: har employee ki salary different ho sakti hai
        self.basic_salary = basic_salary

        # New Employee object create hua, isliye shared count increase kar rahe hain
        Employee.total_employees += 1

    def display_details(self):
        # Instance method: particular employee ke data ke saath kaam karna hai, isliye self
        print("Name       :", self.name)
        print("Employee ID:", self.employee_id)
        print("Department :", self.department)
        print("Basic Salary:", self.basic_salary)

    def calculate_salary(self):
        # Instance method: particular employee ki basic salary use karni hai, isliye self
        bonus_amount = self.basic_salary * Employee.company_bonus / 100  # Current company bonus calculate
        final_salary = self.basic_salary + bonus_amount  # Basic salary + bonus = final salary
        return final_salary  # Calculated salary caller ko return kar rahe hain

    @classmethod
    def change_company_bonus(cls, new_bonus):
        # Class method: bonus poori company/class ka common data hai, isliye cls
        cls.company_bonus = new_bonus  # Sabhi employees ke liye common bonus update

    @classmethod
    def display_company_info(cls):
        # Class method: class-level information access karni hai, isliye cls
        print("Company Bonus:", cls.company_bonus, "%")
        print("Total Employees:", cls.total_employees)

    @staticmethod
    def calculate_tax(salary, tax_percentage):
        # Static method: tax calculation ko employee ya class data ki zarurat nahi
        tax = salary * tax_percentage / 100  # Given salary par tax calculate
        final_salary = salary - tax  # Tax subtract karke final salary calculate
        return final_salary  # Final result caller ko return


# Creating Employee objects
e1 = Employee("Rahul", "E101", "IT", 50000)  # Object 1: apna employee data store karega
e2 = Employee("Priya", "E102", "HR", 60000)  # Object 2: apna employee data store karega
e3 = Employee("Aman", "E103", "Finance", 70000)  # Object 3: apna employee data store karega


# Displaying individual employee information
e1.display_details()  # self = e1, isliye e1 ka data display hoga

print()

e2.display_details()  # self = e2, isliye e2 ka data display hoga

print()


# Calculating salary for a particular employee
salary = e1.calculate_salary()  # self = e1, isliye e1 ki salary par company bonus lagega
print("Final Salary:", salary)

print()


# Changing company-wide bonus
Employee.change_company_bonus(15)  # Class method: bonus poori company ke liye 15% kar raha hai

print()


# Displaying class-level information
Employee.display_company_info()  # Class method: shared class data display karega

print()


# Independent tax calculation
after_tax = Employee.calculate_tax(80000, 10)  # Static method: sirf salary + tax percentage chahiye
print("Salary after 10% tax:", after_tax)