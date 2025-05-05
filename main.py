from product import Product
from product_manager import ProductManager
from cart import Cart
import random

# Kreiramo instancu
pm = ProductManager()

# Dodajemo proizvode
pm.add_product(Product("Mleko",100,50))
pm.add_product(Product("Hleb",55,200))
pm.add_product(Product("Sir",250,25))
pm.add_product(Product("Laptop", 800, 5))
pm.add_product(Product("Telefon", 500, 10))
pm.add_product(Product("Monitor", 200, 7))
pm.add_product(Product("Slusalice", 50, 15))
pm.add_product(Product("Tastatura", 100, 8))

# Prikaz svih proizvoda
pm.products_info()

# Ukupna vrednost inventara
print(f"Ukupna vrednost inventara je: {pm.total_inventory()} dinara")


# Kreiranje instance Cart
cart = Cart()

# Dodavanje tri slucajno odabrana proizvoda u korpu
random_products = random.sample(pm.products,3)

for p in random_products:
    cart.add_to_cart(p)
    
# ispis proizvoda u korpi i ukupno za naplatu

cart.cart_info()
print(f"Ukupna vrednost za naplatu: {cart.total_cart_value()} dinara.")



