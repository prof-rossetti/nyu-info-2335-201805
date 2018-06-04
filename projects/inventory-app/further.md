
# Inventory Management App

## Further Exploration

If you are moving through this project with ease, consider addressing one or more of the following "Further Exploration" challenges, but only after you have finished the core required functionality.

### Validating Price Inputs

For students desiring optional further exploration, the program's "Create" and "Update" operations should validate product information input by the user, focusing on ensuring prices are in the proper numeric format. The program should display a helpful message (e.g. "Please input a price formatted as a number with two decimal places, like 0.77.") when necessary. And the program should prevent a new product from being created if its price is invalid.

### Validating Aisle and Department Inputs

After focusing on validating prices, optionally devise a better system for standardizing aisle and department names, for example by providing the user with a list of existing values for each during the respective parts of the "Create" and "Update" operations.

### Refactoring

For students desiring optional further exploration, the program's source code should be simplified, or "refactored" to contain minimal or no duplications. The program should conform to the "DRY" principle, which means "Don't Repeat Yourself".

### Testing

For students desiring even more optional further exploration, the repository should contain one or more "tests" which communicate and verify the functionality of one or more of the program's functions.

The test file(s) should exist inside a new "tests" directory, and should be implemented using the `pytest` package.

In order to test the application, its source code may first need to be refactored into functions to remove as much source code as possible from the program's global scope. This enables the resulting functions to be individually invoked and tested.

### Relational Database

For students desiring optional further exploration who know SQL, the program should interface with a relational database instead of a CSV file datastore.

> HINT: Maybe try the [PyMySQL](/notes/programming-languages/python/packages/pymysql.md) or [psycopg2](/notes/programming-languages/python/packages/psycopg.md) packages.

Include as many Python and/or SQL scripts as necessary to create and manage the database, and provide appropriate database-related instructions in the `README.md` file.
