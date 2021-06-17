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
        if len(list_of_products) == 0:
            print("No product stored in the database")
        else:
            for product in list_of_products:
                print(product)
    elif op == 3:
        # get a specific product by product id
        id = pyip.inputStr("Enter the product id: ")
        product = productController.get_product_by_product_id(id)
        if len(product.values()) == 0:
            print("Product not found")
        else:
            print(product)
    elif op == 4:
        # remove a specific product by product id
        id = pyip.inputStr("Enter the product id: ")
        result = productController.remove_product_by_product_id(id)
        if result:
            print("SUCCESS: Product removed from the database")
        else:
            print("Could not remove the product")
    elif op == 5:
        # remove all product by product name
        name = pyip.inputStr("Enter the product name: ")
        productController.remove_all_product_by_name(name)
