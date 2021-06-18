import pyinputplus as pyip
from db.config import cursor, mydb
from helpers.helper import check_duplicate_product
from models.Product import Product


class ProductController:

    def __init__(self) -> None:
        """ Default constructor. """
        self.cursor = cursor
        self.KEY_LIST = ["Product ID", "Product Name",
                         "Product Price", "Product QTY"]

    def add_new_product(self, product: Product) -> None:
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
            print("SUCCESS: Product added into the database")
        except AttributeError:
            print("Attribute error in add_new_product method of ProductController")
            exit()

    def get_all_products(self) -> list:
        """
        Fetch all the products from the database
        :return: List of a dictionary
        """

        SQL_QUERY = "SELECT * FROM `product-crud`.`products`"
        returned_list = list()
        self.cursor.execute(SQL_QUERY)
        # inserting all data to returned_list
        for values in self.cursor:
            if values == None:
                break
            payload = dict()  # empty dictionary
            for i in range(1, len(values)):
                payload[self.KEY_LIST[i-1]] = values[i]
            returned_list.append(payload)
        # returning
        return returned_list

    def get_product_by_product_id(self, product_id: str) -> dict:
        """
        Fetch the product from the database by its product_id
        :param product_id: the product_id of that product
        :return: a dictionary of that fetched product
        """
        product = dict()  # empty dictionary
        SQL_QUERY = f"SELECT * FROM `product-crud`.`products` WHERE product_id = '{product_id}'"
        self.cursor.execute(SQL_QUERY)
        datas = self.cursor.fetchone()  # fetched data from database
        if datas == None:
            return product
        # adding data to the dictionary
        for i in range(1, len(datas)):
            product[self.KEY_LIST[i-1]] = datas[i]
        # returning
        return product

    def remove_product_by_product_id(self, product_id: str) -> bool:
        """
        Remove the prodcut from the database. Find the product and then delete it.
        :param product_id: the product_id of that product
        :return: True if succeed else False
        """
        # checking if the given product id is valid or not
        product = self.get_product_by_product_id(product_id)
        if len(product.values()) == 0:
            return False
        # if the given product id is valid
        SQL_QUERY = f"DELETE FROM `product-crud`.`products` WHERE (`product_id` = '{product_id}');"
        self.cursor.execute(SQL_QUERY)
        return True

    def remove_all_product_by_name(self, product_name: str) -> None:
        """
        Remove all the prodcuts from the database. Find the product and then delete it one by one.
        :param product_name: the product_name of that product
        """
        # checking if the given product id is valid or not
        SQL_QUERY = f"DELETE FROM `product-crud`.`products` WHERE product_name = '{product_name}'"
        self.cursor.execute(SQL_QUERY)  # executing the query
        mydb.commit()  # saving the database
        print("SUCCESS: All product deleted from the database"
              + " if there was any with that name")

    def __change_qty_of_a_product(self, product_id: str, value: float) -> bool:
        """
        Change the qty property of a product
        :param product_id: product id of the product
        :param value: value to decrease or increase
        """
        product = self.get_product_by_product_id(product_id)
        if len(product.values()) == 0:
            return False
        # if all OK
        new_qty = product['Product QTY'] + value
        SQL_QUERY = f"UPDATE `product-crud`.`products` SET `product_qty` = '{new_qty}' WHERE (`product_id` = '{product_id}')"
        self.cursor.execute(SQL_QUERY)  # executing the query
        mydb.commit()  # saving the database
        return True

    def increase_qty(self, product_id: str) -> bool:
        """
        increase the qty
        :param product_id: id of that product
        """
        value = pyip.inputFloat("Enter the amount to increase: ")
        return self.__change_qty_of_a_product(product_id, value)

    def decrease_qty(self, product_id: str) -> bool:
        """
        decrease the qty
        :param product_id: id of that product
        """
        value = pyip.inputFloat("Enter the amount to increase: ")
        return self.__change_qty_of_a_product(product_id, (-1) * value)
