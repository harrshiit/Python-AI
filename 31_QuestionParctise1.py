<!-- """PRODUCT STORE
Design and create an online Product Store.
Each product should have a name and a price.
The store should keep track of the total number of products being created.
You should be able to display the details of a product.
You should also be able to calculate the discount on a product based on a given percentage and determine its final price after discount.
Create multiple products and demonstrate all the required functionalities.
""" -->

class Product:

    total_products = 0  # Class variable: sabhi Product objects ka common/shared count

    def __init__(self, name, price):
        self.name = name  # Instance variable: har product ka apna name hota hai
        self.price = price  # Instance variable: har product ka apna price hota hai

        Product.total_products += 1  # Har naya Product create hone par total count increase


    def display_product(self):
        # Instance method: specific product ke name aur price ke saath kaam karna hai
        print("Product Name :", self.name)
        print("Product Price:", self.price)


    @classmethod
    def display_total_products(cls):
        # Class method: total_products poori class ka shared data hai, isliye cls use kar rahe hain
        print("Total Products:", cls.total_products)


    @staticmethod
    def calculate_discount(price, discount_percentage):
        # Static method: calculation ko kisi object (self) ya class data (cls) ki zarurat nahi
        discount_amount = price * discount_percentage / 100
        final_price = price - discount_amount

        return final_price


# Creating Product objects
p1 = Product("Laptop", 50000)  # Object 1: iska apna name aur price hoga
p2 = Product("Mouse", 1000)    # Object 2: iska apna name aur price hoga
p3 = Product("Keyboard", 2000) # Object 3: iska apna name aur price hoga


# Displaying individual product details
p1.display_product()  # Instance method: p1 ke data par kaam karega
p2.display_product()  # Instance method: p2 ke data par kaam karega
p3.display_product()  # Instance method: p3 ke data par kaam karega


# Displaying total number of products
Product.display_total_products()  # Class method: poori class ka shared count display karega


# Calculating discount
final_price = Product.calculate_discount(50000, 10)  # Static method: price aur % se independent calculation

print("Final Price after 10% discount:", final_price)





#Alternate Method 



class Product:

    total_products = 0  # Class variable: sabhi products ka common count

    def __init__(self):
        pass  # Constructor sirf object create hone par run hoga; abhi initial data nahi chahiye

    def set_product(self, name, price):
        self.name = name  # Instance variable: current object ka apna name
        self.price = price  # Instance variable: current object ka apna price

        Product.total_products += 1  # Product details set hote hi total count increase

    def display_product(self):
        print("Product Name :", self.name)  # self se current product ka name access
        print("Product Price:", self.price)  # self se current product ka price access

    @staticmethod
    def calculate_discount(price, percentage):
        # Static method: sirf calculation hai, kisi object/class data ki need nahi
        discount = price * percentage / 100
        return price - discount


# Objects create kiye
p1 = Product()
p2 = Product()
p3 = Product()


# Instance method se har object ki details set ki
p1.set_product("Laptop", 50000)
p2.set_product("Mouse", 1000)
p3.set_product("Keyboard", 2000)


# Har product ki details display
p1.display_product()
p2.display_product()
p3.display_product()


# Class variable ko directly access karke total count
print("Total Products:", Product.total_products)


# Static method se discount calculate
final_price = Product.calculate_discount(50000, 10)
print("Final Price after 10% discount:", final_price)