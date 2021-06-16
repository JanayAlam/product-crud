import os

import mysql.connector
from dotenv import load_dotenv

# loading the dot env file
load_dotenv()


class ProductController:

    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USERNAME"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME"),
            auth_plugin="mysql_native_password"
        )
        self.cursor = self.mydb.cursor()

    def add_new_product(self, product):
        """
        Add a new product into the database
        :param product: Product class instance
        """
        self.cursor.execute(
            f"INSERT INTO `product-crud`.`products` (`product_id`, `product_name`, `product_price`, `product_qty`) VALUES('{product.get_product_id()}', '{product.get_product_name()}', '{product.get_product_price()}', '{product.get_product_qty()}')"
        )
        self.mydb.commit()
        print("Added")
