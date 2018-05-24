

### Further Exploration

If you are moving through this project with ease, consider addressing one or more of the following "Further Exploration" challenges, but only after you have finished the core required functionality.

### Validating User Inputs

For students desiring optional further exploration, the program's "Create" and "Update" operations should validate product information input by the user, focusing on ensuring prices are in the proper numeric format. The program should display a helpful message (e.g. "Please input a price formatted as a number with two decimal places.") when necessary.

After focusing on validating prices, optionally devise a better system for standardizing aisle and department names, and provide the user with a list of available values for each during the "Create" and "Update" operations.

### Refactoring

For students desiring optional further exploration, the program's source code should be simplified, or "refactored" to contain at most a minimal amount of duplication. The program should conform to the "DRY" principle, which means "Don't Repeat Yourself".

### Testing

For students desiring even more optional further exploration, the repository should contain one or more "tests" which communicate and verify the functionality of one or more of the program's functions.

The test file(s) should exist inside a new `tests` directory, and should be implemented using the `pytest` package.

In order to test the program, much of its source code should first be refactored into functions to remove as much source code as possible from the program's global scope. This enables the resulting functions to be individually invoked and tested.
