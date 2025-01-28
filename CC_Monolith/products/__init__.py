from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


# Unoptimized version:
# def list_products() -> list[Product]:
#     products = dao.list_products()
#     result = []
#     for product in products:
#         result.append(Product.load(product))
#     return result

# Optimized version:
def list_products() -> list[Product]:
    return [Product.load(product) for product in dao.list_products()]


# Unoptimized version:
# def get_product(product_id: int) -> Product:
#     return Product.load(dao.get_product(product_id))

# Optimized version:
def get_product(product_id: int) -> Product:
    product_data = dao.get_product(product_id)
    return Product.load(product_data) if product_data else None


# Unoptimized version:
# def add_product(product: dict):
#     dao.add_product(product)

# Optimized version:
def add_product(product: dict):
    if not isinstance(product, dict):
        raise ValueError("Product must be a dictionary")
    dao.add_product(product)


# Unoptimized version:
# def update_qty(product_id: int, qty: int):
#     if qty < 0:
#         raise ValueError('Quantity cannot be negative')
#     dao.update_qty(product_id, qty)

# Optimized version:
def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError("Quantity cannot be negative")
    dao.update_qty(product_id, max(0, qty))
