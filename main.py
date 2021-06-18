# main menu for product crud project
# shows the user the menu and let the user to decide what to do

import pyinputplus as pyip

from controllers.ProductController import ProductController
from helpers.helper import *

if __name__ != "__main__":
    exit()

productController = ProductController()


def inputId():
    """ take product id input from the user and return that value """
    id = pyip.inputStr("Enter the product id: ")
    return id


while True:
    menu_options()
    op = pyip.inputInt(">>> ", min=0, max=9)

    if op == 0:
        # exit the application
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
        id = inputId()
        product = productController.get_product_by_product_id(id)
        if len(product.values()) == 0:
            print("Product not found")
        else:
            print(product)
    elif op == 4:
        # remove a specific product by product id
        id = inputId()
        result = productController.remove_product_by_product_id(id)
        if result:
            print("SUCCESS: Product removed from the database")
        else:
            print("Could not remove the product")
    elif op == 5:
        # remove all product by product name
        name = pyip.inputStr("Enter the product name: ")
        productController.remove_all_product_by_name(name)
    elif op == 6:
        # increasing the qty of a perticular product
        id = inputId()
        result = productController.increase_qty(id)
        if result:
            print("SUCCESS: Product availablity increased")
        else:
            print("Product not found")
    elif op == 7:
        # decreasing the qty of a perticular product
        id = inputId()
        result = productController.decrease_qty(id)
        if result:
            print("SUCCESS: Product availablity decreased")
        else:
            print("Product not found")
    elif op == 8:
        # change the name of a perticular product
        id = inputId()
        pass
    elif op == 9:
        # change the price of a perticular product
        id = inputId()
        pass
