class Product:

    def __init__(self, product_id, product_name, product_price, product_qty) -> None:
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_price = product_price
        self.__product_qty = product_qty

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_product_price(self):
        return self.__product_price

    def get_product_qty(self):
        return self.__product_qty
