# main menu for product crud project
# shows the user the menu and let the user to decide what to do

import pyinputplus as pyip

from controllers.ProductController import ProductController
from helpers.helper import *

if __name__ != "__main__":
    exit()

productController = ProductController()


while True:
    menu_options()
    op = pyip.inputInt(">>> ", min=0, max=9)

    if op == 0:
        print("Exiting...")
        exit()
    elif op == 1:
        # Add a new product
        product = create_product()
        if product != None:
            productController.add_new_product(product)
        else:
            print("Could not create the product")
    elif op == 2:
        # get all product
        list_of_products = productController.get_all_products()
        for product in list_of_products:
            print(product)
