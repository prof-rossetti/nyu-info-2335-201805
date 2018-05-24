# Point-of-Sale App

## Checkpoints

### Checkpoint I - User Inputs

  1. Print a menu which contains a greeting message and a hard-coded number of products and a list of available operations.
  1. Using the aforementioned menu, prompt the user to choose one of the available operations, and print the name of the chosen operation.
  1. Implement a single "handler" function to recognize the chosen operation and invoke one of a handful of new operation-specific functions to perform the chosen operation. For example, if the user chooses "Create", have your "handler" function invoke a function called `create_product()` to print the name of the chosen operation.
  1. Handle invalid operation inputs by displaying a helpful message like "Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'."

After demonstrating your ability to properly prompt the user for inputs, feel free to comment-out all your user input-related code as you move on to implementing and testing the remaining functionality. If you do, remember to un-comment the input-related code and hook it back up to the remaining functionality once implemented.

### Checkpoint II - Reading and Writing to CSV File

#### Reading

  1. Demonstrate your ability to loop through each product in the inventory and print the name of each.
  1. Demonstrate your ability to print the number of products in the inventory.
  1. Re-configure the user input menu to use the real number of products instead of a hard-coded value. This will require you to read the CSV file before prompting the user for inputs.

Hint: read the file to extract and transform the inventory of products into a list of dictionary-like items for further use.

#### Writing

  1. Write some random content to a temporary file, perhaps named `data/writing-stuff.csv`.
  1. Read the existing inventory of products from `products.csv` and write to a separate, temporary file, perhaps named `data/writing-products.csv`.
  1. Read the existing inventory of products from `products.csv` and overwrite that same file with its original contents.

Hint: after compiling and perhaps further manipulating the extracted list of dictionary-like items, loop through the list to write each one to file. Feel free to overwrite the CSV file in this way instead of searching for specific line(s) within it to modify.

### Checkpoint III - CRUD Operations

  1. Implement the "List" operation. Hint: loop through a list of product items like you have done before.
  1. Implement the "Show" operation.
  1. Implement the "Create" operation.
  1. Implement the "Destroy" operation.
  1. Implement the "Update" operation last, as it uses a combination of techniques shared with the "Show" and "Create" operations.

Hint for the "Show", "Destroy", and "Update" operations: before you perform the desired action, you first need to look up a product given its identifier. To do this, you should be able to use list filtering technique similar to what you have done before.

Hint for the "Create" and "Update" operations: you will most likely need to prompt the user to input additional information, like the value for each product attribute.

Hint for "Create", "Update", and "Destroy" operations: as long as you are using a file-writing strategy that loops through each product and writes it to file, it should be sufficient to simply modify or add or remove an item from the existing list of products before writing them.
