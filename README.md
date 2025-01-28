# Monolith-CC-Lab
CC Lab project with optimizations
for cart:
Changes Made:
Replace eval with json.loads: eval is unsafe and can execute arbitrary code. json.loads is safer and specifically for parsing JSON strings.
Reduce Redundant Loops: Combined loops to process contents more efficiently.
Avoid Repeated Access to DAO: Ensured operations in get_cart reduce redundant computations.

for browse: Changes Made:
list_products:
Used a list comprehension for efficiency and conciseness.
get_product:
Added a check to return None if dao.get_product(product_id) is None instead of directly passing it to Product.load.
add_product:
Added input validation to ensure product is a dictionary.
update_qty:
Added an additional safeguard to ensure the quantity is not negative before updating.
