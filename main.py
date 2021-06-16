# main menu for product crud project
# shows the user the menu and let the user to decide what to do


from controllers.ProductController import ProductController
from helpers.helper import *

if __name__ == "__main__":
    productController = ProductController()
    product = create_product()

    if product != None:
        productController.add_new_product(product)
