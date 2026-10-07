# Abstraction has two main purposes:
# 1. Hide unnecessary internal complexity — the user only needs to know what to do, not how it happens internally.
#    Example: when you call payment.pay(), you don’t need to know whether UPI is checking PIN, contacting the bank server,
#    verifying balance, generating a transaction ID, etc. All that complex logic stays hidden inside pay().
# 2. Force a common structure/contract — every payment type should provide the same required method like pay(). UPI, Card, 
# and Cash can implement it differently, but the application can safely use:
# payment.pay()
# So in one line: Abstraction = expose only the necessary operation + hide its complex implementation + ensure
# related classes follow a common 
# required behavior.


# 1 ...Problem with Normal Inheritance & Need for Abstraction
# Normal inheritance in Python
class Payment:
    def pay(self):
        pass                      # Parent has pay(), but no real implementation
class UPI(Payment): # class UPI inherits from Payment
    def pay(self):
        print("UPI Payment")      # UPI decides HOW payment happens
class Card(Payment):
    def pay(self):
        print("Card Payment")     # Card decides HOW payment happens
class Cash(Payment):
    pass                          # Programmer forgot to override pay()
upi = UPI()
upi.pay()                         # UPI Payment
cash = Cash()
cash.pay()        # No error Python uses Payment.pay() Payment.pay() contains only pass  So nothing happens

# We wanted this rule: Every Payment child class MUST implement pay()
# But normal Python inheritance does NOT force that rule.

#but in java  Java, abstraction can enforce it:
# abstract class Payment {

#     abstract void pay();          // Contract:
#                                   // every concrete child MUST implement pay()
# }
# class UPI extends Payment {
#     void pay() {
#         System.out.println("UPI Payment");   // HOW UPI pays
#     }
# }
# class Cash extends Payment {
#     // pay() is missing ❌
# } Java gives an error because Payment already said: abstract void pay();





# 2 ...Solution: Python Abstraction with abc module
#from abc import ABC, abstractmethod

#abc- Abstract Base Classes Is module ka purpose hai Python me abstraction implement karne ke tools dena.

#ABC-ABC ek class hai jo abc module ke andar already defined hai.Hum  apni class ko ABC se
# inherit karwate hain:Sirf ABC likhne se child ko method implement karna compulsory nahi hota
from abc import ABC

class Payment(ABC):

    def pay(self):
        pass
 class Cash(Payment):
    pass
cash = Cash()     # ✅ Allowed
cash.pay()        # kuch nahi hoga 
#so kevl ABC se inherit karne se child ko method implement karna compulsory nahi hota.
#Phir abstractmethod kya karta hai? abstractmethod ek decorator hai.Hum ise kisi method ke upar lagate hain:
from abc import ABC, abstractmethod
class Payment(ABC):               # Abstract Base Class
  @abstractmethod   #Ye method sirf normal method nahi hai.Ye 
    def pay(self):    #ek compulsory abstract method hai.Concrete child class ko isko implement karna padega.
        pass
class UPI(Payment):
    def pay(self):
        print("UPI Payment")      # ✅ requirement fulfilled
upi = UPI()
upi.pay() #output: UPI Payment
class Cash(Payment):
    pass
cash = Cash() #  will give error cannot even craete object of Cash class because it has not implemented 
#abstract method pay() of parent class Payment

# what if using only decorator @abstractmethod without inheriting ABC class
from abc import abstractmethod
class Payment:
   @abstractmethod
    def pay(self):
        pass
class Cash(Payment):
    pass
cash = Cash()   # ✅ Allowed
# Yaha pay() ko @abstractmethod mark kiya gaya hai, but Payment proper abstract class nahi bani 
# because it is not using ABC/ABCMeta. Isliye Python Cash() object creation ko block nahi karta.








#3 But couldn't we do this without abstraction?
# suposse 
class UPI:
    def pay(self):
        print("UPI Payment")
class Card:
    def pay(self):
        print("Card Payment")
class Cash:
    def make_payment(self): # humne yaha method ka naam kuch aur rakha
        print("Cash Payment")
upi = UPI()
card = Card()
upi.pay()      # UPI Payment
card.pay()     # Card Payment
cash = Cash()
cash.make_payment()  # Cash Payment
def checkout(payment): # But suppsoewe craete the checkout system in our codebase,
    payment.pay()
checkout(UPI())      # ✅ UPI Payment
checkout(Card())     # ✅ Card Payment
checkout(Cash())     # ❌ Error 
# therefore abstraction humme  ye formal enforced rule de rha  hai:
#"Agar tum Payment ho, to pay() implement karna compulsory hai."
# So Abstraction helpful  in :
#Consistency→ sab Payment same interface follow karte hain
# Enforced contract → pay() bhool nahi sakte
# Easier polymorphism → payment.pay() sabke saath same way call kar sakte ho
# Safer extension→ future me CreditCard, Wallet, Crypto add karo,unko bhi pay() implement karna padega
# Clear architecture → developer ko Payment class dekhte hi pata chal jayega ki required behavior kya hai
# Also it helpful in hiding complex implementation details from the caller. 
# Caller doesn't need to know whether internally it uses:
# UPI API  card gateway bank validation  OTP   network request  database
#The exposed operation is simply: pay()






#4. What can an Abstract Class contain?
# Abstract class ke andar sirf abstract methods hi nahi hote. Ye dono contain kar sakti hai:
# 1. Abstract methods  → child ko implement karna compulsory
# 2. Normal methods    → child directly inherit karke use kar sakta hai
from abc import ABC, abstractmethod
class Payment(ABC):
     def start_payment(self): #normal method
#Why useful? Because jo functionality sab payment types me common hai, wo parent me ek hi baar likh sakte ho.
        print("Checking payment details...")
        print("Generating transaction ID...")
    @abstractmethod
    def pay(self):# abstract method
        pass
class UPI(Payment):

    def pay(self):
        print("Opening UPI application")

upi = UPI()
upi.start_payment()   # common functionality
upi.pay()             # UPI-specific functionality
# Checking payment details...
# Generating transaction ID...
# Opening UPI application







#Code  Example 
from abc import ABC, abstractmethod
# Abstraction: every storage type must provide upload()
class StorageProvider(ABC):

    @abstractmethod
    def upload(self, file_name):
        pass
# AWS-specific implementation
class AWSStorage(StorageProvider):

    def upload(self, file_name):
        print(f"{file_name} uploaded to AWS")
# Google-specific implementation
class GoogleStorage(StorageProvider):

    def upload(self, file_name):
        print(f"{file_name} uploaded to Google Cloud")
# Local machine implementation
class LocalStorage(StorageProvider):

    def upload(self, file_name):
        print(f"{file_name} saved locally")


# Business logic does not care which storage is being used
class ResumeService:

    def __init__(self, storage):
        self.storage = storage

    def upload_resume(self, file_name):
        self.storage.upload(file_name)   # Calls AWS/Google/Local upload()


# We can switch storage without changing ResumeService
storage = AWSStorage()
# storage = GoogleStorage()
# storage = LocalStorage()

resume = ResumeService(storage)

resume.upload_resume("harshit_resume.pdf")
#here StorageProvider = HOW to store a file  & ResumeService   = WHAT to do with a resume

# you can put the constructor and upload_resume() inside StorageProvider. Technically it would work.
from abc import ABC, abstractmethod
class StorageProvider(ABC):
   def __init__(self, user_name, file_name):
        self.user_name = user_name
        self.file_name = file_name

    @abstractmethod
    def upload(self):
        pass

    def upload_resume(self):
        print(f"Uploading resume for {self.user_name}")
        self.upload()
# The problem appears when the application grows. Suppose later ResumeService has to do:
# validate PDF
# check file size
# save user ID in DB
# rename resume
# send notification
# update profile
# Now we have to integrate all this in storage  provider. But storage provider is only responsible for HOW to store a file, not WHAT to do with a resume.
# we have  to put the things like whree it belongs. So we can create a separate class ResumeService to handle the WHAT
# to do with a resume and keep StorageProvider only for HOW to store a file.
#we can add functions like 
# upload()
# delete()
# download()
# check_file()
# get_url() in strorage provider class and keep the ResumeService class only for the WHAT to do with a resume.