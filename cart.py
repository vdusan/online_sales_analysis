from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []
        
    def add_to_cart(self, product):
        self.cart_items.append(product)
        
    def total_cart_value(self):
        return sum(item.price * item.quantity for item in self.cart_items)
    
    
    def cart_info(self):
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            print("Proizvodi u korpi: ")
            for item in self.cart_items:
                print(item.info())
        
        
    