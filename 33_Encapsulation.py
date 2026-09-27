# // Encapsulation is the OOP concept of bundling data (variables) and the methods
# //  that operate on that data inside a class, while controlling how 
# that data can be accessed or modified from outside the class.

#  1. WHY DO WE NEED ENCAPSULATION?
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BankAccount(10000)
print(account.balance)      # 10000
account.balance = -5000  # The balance can be directly modified from outside the class.
print(account.balance)      # -5000
# This is a problem because: 1. Anyone can directly change the data. 2. Invalid values can be assigned.
# The class has no control over how its data is modified.




# 2. HOW TO DEAL WITH THe  problem -> ACCESS MODIFIERS Access modifiers define how the data and methods  of a class can be accessed from outside the class.
# Common access levels are: Public  Protected  Private
#PUBLIC ACCESS MODIFIER
class BankAccount:

    def __init__(self, balance):
        self.balance = balance  # here balaance is public becuse no underscore is used before the variable name
     def deposit(self, amount): # method  create to deposit money into the account
        if amount > 0:
            self.balance += amount

account = BankAccount(10000) # creating an object of the class BankAccount with initial balance of 10000
print(account.balance)   # 10000 Because balance is public,# we can directly access it using the object.
account.balance = 15000  # We can also directly modify it.
print(account.balance)          # 15000
account.deposit(5000)  # We can also access the public method directly.
print(account.balance)          # 20000

account.balance = -5000  # problem: We can directly modify the balance to an invalid value.
print(account.balance)          # -5000  The class cannot prevent this direct modification because balance is PUBLIC.





#  PROTECTED ACCESS MODIFIER
# In Python, a single underscore (_) is used to indicate that a member is PROTECTED / intended for internal use.
class BankAccount:
       def __init__(self, balance):
        self._balance = balance        # Protected attribute
       def _show_balance(self):       # Protected method
        return self._balance
account = BankAccount(10000)
# We CAN technically access a protected member  from outside the class in Python. becuse 
# Python does not enforce access restrictions. However, 
# it is a convention that indicates that the member is  protected / intended for internal use 
# like java it resticted the protected members to be accessed only within the class and its subclasses. 
# not from outside the class. but python does not enforce this restriction.
# it is only a convention that indicates that the member is intended for internal use and 
# should not be accessed directly from outside the class.
print(account._balance)          # 10000
account._balance = -5000   # We can even modify it.
print(account._balance)          # -5000 which is a problem because the class cannot prevent this direct modification because _balance is PROTECTED.






# PRIVATE ACCESS MODIFIER
# In Python, a double underscore (__) at the beginning of a variable name is used to indicate a PRIVATE member.
class BankAccount:
     def __init__(self, balance):
        self.__balance = balance         # Private attribute
    def get_balance(self):             # Public method to access the private data
        return self.__balance
    def deposit(self, amount):           # Public method to modify the private data
          if amount > 0:
            self.__balance += amount
         else:
           print(" wrong deposit")

account = BankAccount(10000)
print(account.get_balance())       # 10000  # We can access the private data through a public method.
print(account.__balance)     # ❌ AttributeError cannot directly access private data from outside the class. This will raise an AttributeError.
account.deposit(5000)
print(account.get_balance())       # 15000
# NAME MANGLING
# Suppose we write:  self.__balance   inside:    BankAccount
# Python internally changes the name approximately to:
#  _BankAccount__balance     This is called NAME MANGLING.
# Therefore, this normally fails: account.__balance
# But this can technically access the mangled attribute:  account._BankAccount__balance
print(account._BankAccount__balance)    # 15000 
# So __ does NOT create absolute security. It mainly prevents accidental direct access and
# avoids name conflicts in inheritance.
#  therefore Therefore, Python does not have Java-style absolute private access control.Python has no strictly enforced private access 
# modifier like Java. __name provides name-mangled private-like behavior.







#  GETTER AND SETTER When data is kept private, we should not directly access modify it from outside the class.
# Instead, we can provide methods to: 1. GET  -> read/access the data  2. SET  -> modify/update the data
#
# These methods are commonly called:
#
# Getter -> method used to get/read a value
# Setter -> method used to set/update a value
class BankAccount:
      def __init__(self, balance):
        self.__balance = balance          # Private attribute
      def get_balance(self):    # Getter method Used to read the private balance.
          return self.__balance
      def set_balance(self, balance):     # Setter methodUsed to modify the private balance.
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance!")
account = BankAccount(10000)
print(account.__balance)        # Direct access is not allowed normally:
print(account.get_balance())      # 10000 # Instead, use the getter:
 account.__balance = -5000       ❌
account.set_balance(15000)      # Use the setter:
print(account.get_balance())      # 15000
account.set_balance(-5000)    # The setter can also prevent invalid values.
print(account.get_balance())      # 15000







# FINAL PRACTICAL / INDUSTRY-STYLE EXAMPLE USER ACCOUNT SYSTEM
# In a real application, user information may containsensitive data such as:  username
#     email password account status
# We should NOT allow outside code to freely modify
class UserAccount:
     def __init__(self, username, email, password):
          self.username = username# Public attribute  These can be accessed normally.
          self.email = email
          self.__password = password # Private attrribute Password should not be directly exposed.
          self.__is_active = True           # Internal account state

    def change_password(self, old_password, new_password):
         if old_password != self.__password:         # First verify the old password.
            print("Incorrect current password.")
            return
         if len(new_password) < 8:         # Validate the new password.
            print("Password must contain at least 8 characters.")
            return
         self.__password = new_password        # Update password only after validation.
         print("Password changed successfully.")
    # now creating objewct and  initializing the data
user = UserAccount(
    "harshit",
    "harshit@example.com",
    "password123"
)
print(user.username) # Public data can be accessed normally.
print(user.email)

user.change_password(
    "password123",
    "newpassword123"
)
user.change_password(
    "wrongpassword",
    "anotherpassword"
)  # Output:Incorrect current password.
