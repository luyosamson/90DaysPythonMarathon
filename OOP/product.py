# Build a class called "Product" with attributes like name, price, and quantity.
# Implement methods to calculate the total cost of the product
#based on the quantity purchased and display the product details.
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def product_cost(self):
        total=self.price*self.quantity
        return total
    def product_details(self):
        print(f"NAME:{self.name} UNIT PRICE: {self.price} QUANTITY :{self.quantity}")
    
product1=Product("Book",500,4)
print("Total price",product1.product_cost())
product1.product_details()