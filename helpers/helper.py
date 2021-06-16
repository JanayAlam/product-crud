import pyinputplus as pyip
from db.config import cursor
from errors.DuplicateValueError import DuplicateValueError
from models.Product import Product


def create_product() -> Product:
    """
    Create a Product class instance by taking input from the user
    :return: Product class instance
    """
    try:
        product_id = pyip.inputStr("Enter product id: ")
        # finding duplicates
        is_valid = check_duplicate_product(product_id)
        if (is_valid):
            raise DuplicateValueError("Product id must be unique.")
        # if all OK
        product_name = pyip.inputStr("Enter product name: ")
        product_price = pyip.inputNum("Enter product price: ")
        product_qty = int(pyip.inputNum("Enter product availability: "))
        # returning the product payload
        return Product(product_id, product_name, product_price, product_qty)
    except ValueError:
        print("Couldn't convert the qty variable to integer")
        return None
    except DuplicateValueError as e:
        print(e.get_message())
        print("Try again.")
        return None


def check_duplicate_product(product_id: str) -> bool:
    """
    Fetch data from the database with given string parameter. Check if there is any data or not.
    :param product_id: string type product id
    """
    SQL_QUERY = f"SELECT * FROM `product-crud`.`products` WHERE product_id ='{product_id}'"
    rows = cursor
    rows.execute(SQL_QUERY)
    # fetched length is greater than 0 means there is a duplicate id
    return len(rows.fetchall()) != 0


def menu_options():
    pass
