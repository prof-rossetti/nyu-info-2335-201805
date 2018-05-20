# Python Datatypes Exercise ([Video Walkthrough](https://youtu.be/_w1hRdAD4LQ))

## Objectives

... _______

## Instructions

Write a Python script that will transform the following information input (i.e. `products`) into the desired output, below:

```py
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
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
```

... into the following synthesized information output:

    --------------
    THERE ARE 20 PRODUCTS:
     + All-Seasons Salt ($4.99)
     + Chocolate Fudge Layer Cake ($18.50)
     + Chocolate Sandwich Cookies ($3.50)
     + Cut Russet Potatoes Steam N' Mash ($4.25)
     + Dry Nose Oil ($21.99)
     + Fresh Scent Dishwasher Cleaner ($4.99)
     + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
     + Green Chile Anytime Sauce ($7.99)
     + Light Strawberry Blueberry Yogurt ($6.50)
     + Mint Chocolate Flavored Syrup ($4.50)
     + Overnight Diapers Size 6 ($25.50)
     + Peach Mango Juice ($1.99)
     + Pizza For One Suprema Frozen Pizza ($12.50)
     + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
     + Pure Coconut Water With Orange ($3.50)
     + Rendered Duck Fat ($9.99)
     + Robust Golden Unsweetened Oolong Tea ($2.49)
     + Saline Nasal Mist ($16.00)
     + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
     + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)
    --------------
    THERE ARE 10 DEPARTMENTS:
     + Babies (1 products)
     + Beverages (5 products)
     + Dairy Eggs (1 products)
     + Dry Goods Pasta (1 products)
     + Frozen (4 products)
     + Household (1 products)
     + Meat Seafood (1 products)
     + Pantry (2 products)
     + Personal Care (2 products)
     + Snacks (2 products)

### Setup

Create a new directory on your desktop or some other place you will remember, and name it "python-datatypes" then navigate there from the command-line:

```shell
# Mac OS:
mkdir ~/Desktop/python-practice
cd ~/Desktop/python-practice

# Windows OS:
mkdir C:\Users\YOUR_USERNAME\Desktop\python-practice
cd C:\Users\YOUR_USERNAME\Desktop\python-practice
```

Within the directory, create a new file called `groceries.py`. In this file, place the following code:

```python
# groceries.py

import code

products = [] #<-- Copy and paste the provided products list here (see above!)

print(products)

# code.interact(local=locals())
```

Run the script to see it print the list of products.

Great, now you are ready to move on to the next step, so commit your code:

```shell
git add .
git commit -m "Setup new repository"
```

Un-comment the last line in your Python script - the one containing `code.interact(local=locals())`. This is known as "dropping a breakpoint" into your program.

Run the script again to enter an interactive debugging console. From within this console you should be able to access the `products` variable. When you are done exploring, type `exit()` to quit.

### Implementation

Iteratively revise and re-run the script to implement desired functionality. Use the breakpoint only when you find it helpful, otherwise keep it commented-out.

When you successfully demonstrate your script's ability to perform one or more component pieces of desired functionality, commit your changes before moving on to the next step. Your history of commit messages should roughly resemble the checkpoint steps below.

#### Checkpoint I - Printing Products

Steps:

  1. Print the number of products.
  2. Print the name of each product.
  3. Print in alphabetical order the name of each product.
  4. Print in alphabetical order the name of each product, and include its price rounded to two decimal places.

#### Checkpoint II - Printing Departments

Steps:

  5. Print the number of unique departments.
  6. Print the name of each unique department.
  7. Print in alphabetical order the name of each unique department.
  8. Print in alphabetical order the name of each unique department, as well as the number of products associated with that department.

## Submission Instructions

### Step 1 - Creating a new Project Repo

Use the GitHub.com online interface to create a new GitHub repository under your control named something like "python-datatypes". When you create a new repository, in order to easily use the GitHub.com online interface to manage files, check the box to **Initialize this repository with a README**. Once the repository is created, add a file to it called `groceries.py`. Paste your Python script into that file, then save and commit it. At this time you should be able to view your instructions online at your project repository's URL.

### Step 2 - Forking the Course Repo

If you have not yet already forked the course repository, do so now.

Otherwise, if you have already forked the course repository (i.e. if you have already submitted a previous exercise), then you will need to update your existing fork instead.


### Step 2 - Submitting a Pull Request

Add a new record to the [submissions file](submissions.csv) in your , to include your GitHub username and the repository's URL (e.g. https://github.com/s2t2/python-datatypes). After updating your own fork, you will need to submit a Pull Request for your content to be accepted into the main course repository.
