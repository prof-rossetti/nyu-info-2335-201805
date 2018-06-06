import csv
import os

# Author: Eunah Cho(ID: lunarcea)

def menu(username, products_count):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
        'Reset'   | Reset the CSV file.
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu


def read_products_from_file(filename="products_default.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    # print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # print(row["name"], row["price"])
            products.append(dict(row))
    return products

# print(read_products_from_file("products_default.csv"))


#def write_products_to_file(filename="products.csv", products=[]):
def write_products_to_file(filename, products):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    # print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader() # uses fieldnames set above
        for product in products:
            # print(product)
            writer.writerow(product)

products = read_products_from_file("products_default.csv")

write_products_to_file("products.csv", products)


def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file()
    print(len(products))
    write_products_to_file(filename, products)

def run():

    # First, read products from file...
    products = read_products_from_file()

    # Then, prompt the user to select an operation...
    number_of_products = len(products)
    my_menu = menu(username="@lunarcea", products_count=len(products))
    operation = input(my_menu)
    print("YOU CHOSE:", operation)

    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...

    operation = operation.title()
    if operation == "List":
       print("-----------------------------------")
       print("LISTING PRODCUTS")
       print("-----------------------------------")
       for p in products:
           print("      " + p["id"] + " " + p["name"])

    elif operation == "Show":
        print("-----------------------------------")
        print("SHOWING A PRODUCT")
        print("-----------------------------------")
        product_id = input("Hey, what's the identifiers of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        print(matching_product)

    elif operation == "Create":
        new_id = int(products[-1]["id"]) + 1
        new_product = {
            "name": "New Product",
            "aisle": "New Aisle",
            "department": "New Dept",
            "price": 100.00
        }
        products.append(new_product)
        print("-----------------------------------")
        print("CREATING A PRODUCT", new_product)
        print("-----------------------------------")
        print(product)


    elif operation == "Update":
        product_id = input("Hey, what's the identifiers of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        csv_headers = ["id", "name", "aisle", "department", "price"]
        def editable_product_attributes():
            attribute_names = [attr_name for attr_name in csv_headers if attr_name != "id"] # adapted from: https://stackoverflow.com/questions/25004347/remove-list-element-without-mutation
            return attribute_names
        def is_valid_price(my_price):
            try:
                float(my_price)
                return True
            except Exception as e:
                return False
        if matching_product == None: product_not_found()
        else:
            for attribute_name in editable_product_attributes():
                new_val = input(f"OK. What is the product's new '{attribute_name}' (currently: '{matching_product[attribute_name]}'): ")
                if attribute_name == "price" and is_valid_price(new_val) == False:
                    product_price_not_valid()
                    return
                matching_product[attribute_name] = new_val
        def update_product(product):
            update_product(product)
        # new_price = 200.00
        # new_price = matching_product["price"] = new_price
        print("-----------------------------------")
        print("UPDATING A PRODUCT", matching_product)
        print("-----------------------------------")


    elif operation == "Destroy":
        product_id = input("Hey, what's the identifiers of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        del products[products.index(matching_product)]
        print("-----------------------------------")
        print("DELETING A PRODUCT")
        print("-----------------------------------")
        print(product)


    elif operation == "Reset":
        reset_products_file()
    else:
        print("OOPS, unrecognized operation, please select one of 'List', 'Show', 'Create', 'Update', 'Destroy' or 'Reset'")

    # Finally, save products to file so they persist after script is done...
    write_products_to_file("products.csv", products)

menu("@luanrcea", len(products))

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
