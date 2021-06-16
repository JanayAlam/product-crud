from db.config import cursor, mydb
from helpers.helper import check_duplicate_product
from models.Product import Product


class ProductController:

    def __init__(self) -> None:
        """ Default constructor. """
        self.cursor = cursor

    def add_new_product(self, product: Product):
        """
        Add a new product into the database
        :param product: Product class instance
        """
        try:
            # all field string
            fileds = "`product_id`, `product_name`, `product_price`, `product_qty`"
            # all values
            values = (f"'{product.get_product_id()}', '{product.get_product_name()}',"
                      + f"'{product.get_product_price()}', '{product.get_product_qty()}'")
            # sql query executing
            self.cursor.execute(
                f"INSERT INTO `product-crud`.`products` ({fileds}) VALUES({values})"
            )
            # saving
            mydb.commit()
            # printing the message
            print("Added")
        except AttributeError:
            print("Attribute error in add_new_product method of ProductController")
            exit()
