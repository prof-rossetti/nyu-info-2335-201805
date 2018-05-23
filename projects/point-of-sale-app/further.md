# Point-of-Sale App

## Further Exploration

If you are moving through this project with ease, consider addressing one or more of the following "Further Exploration" challenges, but only after you have finished the core required functionality.

### Validating User Inputs

For students desiring optional further exploration, the program should also validate the identifiers input by the clerk, displaying to the clerk a helpful message (e.g. "Hey, are you sure that product identifier is correct? Please try again!") if there are no products matching the given identifier.

### Writing Receipts to File

For students desiring even more optional further exploration, the program should also output the receipt information into a new `.txt` file saved somewhere in the project directory. The clerk's printer-connected computer should be able to actually print a paper receipt from the information contained in this file. The text file should be named according to the date and time the checkout process started (e.g. `/receipts/2017-07-04-15-43-13-579531.txt`, where the numbers represent the year, month, day, 24-hour-style hour, minute, second, and milliseconds/microseconds, respectively).

> NOTE: if you are using version control, you should exclude these receipt files from being tracked (a.k.a. "gitignore" them).

See [Python file management](/notes/programming-languages/python/file-management.md) for examples of how to write to file.

### Handling Pricing per Pound

For students desiring even more optional further exploration, add a new product to the list. Name it "Professor Rossetti's Bananas" and assign it other attribute values as desired. Assign it a price of `0.79`, but add another attribute called something like `price_per` to indicate the item is priced per "pound". Update all the other product dictionaries to match the new structure, indicating they are priced per "item". Finally, when running the program, if the clerk inputs the identifier of the bananas (or any other item that is priced by pound), the program should ask the clerk to input the number of pounds (e.g. `2.2`), then the program should calculate the price accordingly.
