'''Scenario:
 
You are building the backend logic of a product and order management system for an e-commerce platform like Amazon or Flipkart. The system needs to handle products, users, payments, discounts, and different order behaviors dynamically.
 
Q1. Product Search System (Static Polymorphism)
 
Problem Statement:

Implement a class ProductSearch that allows searching products with different combinations of criteria (name, category, price range).
 
Requirements:
 
Use default arguments and/or *args, **kwargs to simulate method overloading.
 
Allow the following types of searches:
 
Only by name
 
Name and category
 
Name, category, and price range
 
 
Q2. Cart System with Quantity Variations (Static Polymorphism)
 
Problem Statement:

Design a class Cart that can add multiple products with variable quantities using *args or **kwargs.
 
Requirements:
 
Add multiple products at once with name and quantity
 
Simulate static polymorphism using variable arguments
 
 
Q3. Discount Application (Static Polymorphism)
 
Problem Statement:

Create a class Discount that allows applying different types of discounts:
 
Flat discount
 
Percentage discount
 
Buy One Get One
 
Use static polymorphism to overload the method using default parameters or *args
 
 
Q4. Payment System (Dynamic Polymorphism)
 
Problem Statement:

Implement a base class Payment and subclasses CreditCardPayment, UPIPayment, and CODPayment. Each should override a method pay().
 
Requirements:
 
Override pay() method in each class to simulate different payment methods

 '''
# Q1. Product Search System (Static Polymorphism)
class ProductSearch:
    def search(self, *args, **kwargs):
        if "name" in kwargs and "category" not in kwargs and "price_range" not in kwargs:
            print(f"Searching by Name: {kwargs['name']}")
        elif "name" in kwargs and "category" in kwargs and "price_range" not in kwargs:
            print(f"Searching by Name: {kwargs['name']} and Category: {kwargs['category']}")
        elif "name" in kwargs and "category" in kwargs and "price_range" in kwargs:
            low, high = kwargs["price_range"]
            print(f"Searching by Name: {kwargs['name']}, Category: {kwargs['category']}, "
                  f"Price between {low} and {high}")
        else:
            print("Invalid search criteria")


# Q2. Cart System with Quantity Variations (Static Polymorphism)
class Cart:
    def __init__(self):
        self.items = {}

    def add_products(self, **kwargs):
        for product, qty in kwargs.items():
            self.items[product] = self.items.get(product, 0) + qty
        print("Cart Updated:", self.items)


# Q3. Discount Application (Static Polymorphism)
class Discount:
    def apply_discount(self, *args):
        if len(args) == 2 and args[0] == "flat":
            print(f"Flat discount of ₹{args[1]} applied")
        elif len(args) == 2 and args[0] == "percent":
            print(f"Percentage discount of {args[1]}% applied")
        elif len(args) == 1 and args[0] == "bogo":
            print("Buy One Get One offer applied")
        else:
            print("Invalid discount type")


# Q4. Payment System (Dynamic Polymorphism)
class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must override this method")


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CODPayment(Payment):
    def pay(self, amount):
        print(f"Cash on Delivery selected for ₹{amount}")


# ---------------- TESTING ----------------
if __name__ == "__main__":
    print("===== Product Search =====")
    ps = ProductSearch()
    ps.search(name="iPhone")
    ps.search(name="iPhone", category="Electronics")
    ps.search(name="iPhone", category="Electronics", price_range=(50000, 100000))

    print("\n===== Cart System =====")
    cart = Cart()
    cart.add_products(iPhone=2, Laptop=1, Charger=3)

    print("\n===== Discount System =====")
    d = Discount()
    d.apply_discount("flat", 500)
    d.apply_discount("percent", 10)
    d.apply_discount("bogo")

    print("\n===== Payment System =====")
    payments = [CreditCardPayment(), UPIPayment(), CODPayment()]
    for p in payments:
        p.pay(2500)
