# Python Datatypes Exercise

## Objectives

This exercise provides a tangible set of target outcomes
to help focus our energies and attentions as we explore the [Python programming language](/notes/programming-languages/python/notes.md)
for the first time.

The exercise is divided into sequential incremental challenges
which provide an example of how to break-up a larger problem into into smaller, more manageable pieces.

After completing this exercise, we will have gained familiarity with common
Python [datatypes](/notes/programming-languages/python/datatypes.md) like
[booleans](/notes/programming-languages/python/datatypes/booleans.md),
[numbers](/notes/programming-languages/python/datatypes/numbers.md),
[strings](/notes/programming-languages/python/datatypes/strings.md),
[lists](/notes/programming-languages/python/datatypes/lists.md),
and [dictionaries](/notes/programming-languages/python/datatypes/dictionaries.md).
And we will have laid a foundation for our continuing work with these datatypes over the rest of the semester.


## Instructions

Write a Python script to synthesize and transform a provided information input (i.e. the raw `products` list, below)
into the following desired information output:

    --------------
    THERE ARE 20 PRODUCTS:
    --------------
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
    --------------
     + Babies (1 product)
     + Beverages (5 products)
     + Dairy Eggs (1 product)
     + Dry Goods Pasta (1 product)
     + Frozen (4 products)
     + Household (1 product)
     + Meat Seafood (1 product)
     + Pantry (2 products)
     + Personal Care (2 products)
     + Snacks (2 products)

### Setup

Create a new directory on your Desktop called "python-datatypes", then navigate there from the command-line.

Within that directory, create a new file called `groceries.py` and place inside the following code:

```python
# groceries.py

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

print(products)

# TODO: write some Python code here to produce the desired output
```

Run the script to see it print the list of products:

```sh
# For Homebrew-installed Python 3.x on Mac OS:
python3 groceries.py

# All others:
python groceries.py
```

Great, now you are ready to start the exercise.

> If you plan on submitting this exercise for extra credit,
now would be a good time to create a new Git repository via the GitHub.com online interface
to represent your submittable work product.
After creating the repository, add the `groceries.py` file to it.
You will be revising and "committing" changes to this file periodically throughout the course of this exercise
until it finally achieves the desired functionality. Otherwise, if you would rather focus solely on learning Python and don't feel comfortable working with GitHub yet, ignore references to "committing" in the instructions below.

### Checkpoints

Iteratively revise and re-run the script to implement desired functionality.

When you successfully demonstrate your script's ability to perform one or more component pieces of desired functionality (i.e. "challenges"), commit your changes before moving on to the next step.
After you are done, your repository's history of commit messages should roughly resemble the checkpoint steps below.

If you need help or inspiration, consider following along with this [Screencast](https://www.youtube.com/watch?v=TtDWY-g8IFM) which depicts one possible solution.

#### Checkpoint 1 - Printing Products

Challenges:

  1. Print all products (already done for you!).
  2. Print the first product.
  3. Print the name of the first product.
  4. Print the number of products.
  5. Print the name of each product.
  6. Print in alphabetical order the name of each product.
  7. Print in alphabetical order the name of each product, and include its price rounded to two decimal places.

#### Checkpoint 2 - Printing Departments

Challenges:

  8. Print the number of unique departments.
  9. Print the name of each unique department.
  10. Print in alphabetical order the name of each unique department.
  11. Print in alphabetical order the name of each unique department, as well as the number of products associated with that department.
  12. Print in alphabetical order the name of each unique department, as well as the number of products associated with that department, and properly differentiate between "products" plural and "product" singular, depending on how many there are.

## Submission Instructions

> Submission of this exercise is optional. Students who submit a full solution before the beginning of the third class will receive extra credit. By this time, students should be able to replicate the submission instructions for the "Human Software" exercise, also abbreviated below.

### Step 1 - Creating a new Project Repo

Use the GitHub.com online interface to create a new GitHub repository under your control
named something like "python-datatypes".
When you create a new repository, in order to easily use the GitHub.com online interface to manage files,
check the box to **Initialize this repository with a README**.
Once the repository is created, add a file to it called `groceries.py`.
Paste your Python script into that file, then save and commit it.
At this time you should be able to view your file online at your project repository's URL.

### Step 2 - Forking the Course Repo

If you have not yet already forked the course repository, do so now.

Otherwise, if you have already forked the course repository
(i.e. if you have already submitted a previous exercise),
then you will need to update your existing fork instead.
To do this from the GitHub.com online interface, delete your fork from the repository's "Settings" menu, then re-fork it. There are easier ways to do this from the command-line, but we will get to that later.

### Step 3 - Submitting a Pull Request

Add a new record to the [submissions file](submissions.csv),
to include your GitHub username and the repository's URL (e.g. `https://github.com/YOUR_USERNAME/python-datatypes`).
Finally, submit a Pull Request
for your content to be accepted into the main course repository.
