from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        """Dodavanje novog proizvoda"""
        self.products.append(product)
        
    def products_info(self):
        """ Izlistava sve proizvode """
        for p in self.products:
            print(p.info())
            
    def total_inventory(self):
        """ Ukupna vrednost inventara"""
        return sum(p.price * p.quantity for p in self.products)
    
    
        

            
    