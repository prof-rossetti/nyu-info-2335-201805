# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatobes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

product_list = []
#reference: https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
import datetime #date time for now
now = datetime.datetime.now()

while True:
    product_id = input("Please input a product identifier between 1 and 20, or 'DONE' if there are no more items: ")
    #input default is string.  Need to convert to int


    if product_id == "DONE" or product_id == "done" or product_id == "Done":
        break
#Invalid entry: Out of range
    if int(product_id) <1 or int(product_id)> 20:
        quit("Get your numbers straight and try again")

    else:
        product_list.append(int(product_id))

line = "--------------------------------------------------------------------------------------"
company = "Jeff's Grocery"
web =           "Web:     https://www.wholefoodsmarket.com/"
Phone =         "Phone:   206-266-1000"
Address =       "Address: 1200 12th Ave. South, Suite 1200 • Seattle, WA 98144-2734"
Checkout_time = "Time:    " + str(now.strftime("%Y-%m-%d %H:%M"))

#Print receipt heading
print(line)
print(company.center(76,' '))
print(line)
print(web)
print(Phone)
print(Address)
print(Checkout_time)
print(line)
print("Shopping Cart Items:")

#Matching the inputed product from product to product_list
def matching_product(product_identifier):
    product_list = [p for p in products if p["id"]==product_identifier] #List comprehension,
    return product_list[0] #assume unique identifier, therefore, return the first match.

subtotal_price = 0

for each_item in product_list:
    product = matching_product(each_item) #new product
    subtotal_price += product["price"] #C++ +=
    print("  +  " + str(product["id"]) + ". " + product["name"] +"  ("+ str('${0:.2f}'.format(product["price"]))+ ")")

print(line)
print("Subtotal:                "+ str('${0:.2f}'.format(subtotal_price)))
print("Seattle Sales Tax (9.6%): "+ str('${0:.2f}'.format(subtotal_price*.096)))
print("Total:                   "+ str('${0:.2f}'.format(subtotal_price*1.096)))
print(line)
print("Thank you for shopping at Jeff's Grocery!, Shop us online at www.amazon.com")

# Writing to file
file_name = "my_message.txt" # refers to a file path relative to the path from which you invoke your your script.

with open(file_name, "w") as file: # NOTE: "w" means "open the file for writing"
    file.write(line +"\n")
    file.write(company.center(76,' ')+"\n")
    file.write(line+"\n")
    file.write(web+"\n")
    file.write(Phone+"\n")
    file.write(Address+"\n")
    file.write(Checkout_time+"\n")
    file.write(line+"\n")
    file.write("Shopping Cart Items:"+"\n")
    for each_item in product_list:
        product = matching_product(each_item) #new product
        #subtotal_price += product["price"] #C++ +=
        file.write("  +  " + str(product["id"]) + ". " + product["name"] +"  ("+ str('${0:.2f}'.format(product["price"]))+ ")"+"\n")

    file.write(line+"\n")
    file.write("Subtotal:                "+ str('${0:.2f}'.format(subtotal_price))+"\n")
    file.write("Seattle Sales Tax (9.6%):"+ str('${0:.2f}'.format(subtotal_price*.096))+"\n")
    file.write("Total:                   "+ str('${0:.2f}'.format(subtotal_price*1.096))+"\n")
    file.write(line+"\n")
    file.write("Thank you for shopping at Jeff's Grocery!, Shop us online at www.amazon.com")
