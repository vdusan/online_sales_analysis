from product import Product
from product_manager import ProductManager

# Kreiramo instancu
pm = ProductManager()

# Dodajemo proizvode
pm.add_product(Product("Mleko",100,50))
pm.add_product(Product("Hleb",55,200))
pm.add_product(Product("Sir",250,25))

# Prikaz svih proizvoda
pm.products_info()

# Ukupna vrednost inventara
print(f"Ukupna vrednost inventara je: {pm.total_inventory()} dinara")



