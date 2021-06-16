import pyinputplus as pyip
from models.Product import Product


def create_product() -> Product:
    """
    Create a Product class instance by taking input from the user
    :return: Product class instance
    """
    try:
        product_id = pyip.inputStr("Enter product id: ")
        product_name = pyip.inputStr("Enter product name: ")
        product_price = pyip.inputNum("Enter product price: ")
        product_qty = int(pyip.inputNum("Enter product availability: "))

        return Product(product_id, product_name, product_price, product_qty)
    except ValueError:
        print("Couldn't convert the qty variable to integer")
        exit()


def menu_options():
    pass
