# API Client Exercise

> Prerequisites: [Inventory Management App](/projects/inventory-app/project.md), [APIs Overview](notes/software/apis.md), [Web Requests Exercise](/exercises/web-requests/exercise.md)

Previously we implemented the Inventory Management App using a local CSV file datastore. This allowed managers at different groceries stores to keep their own inventory of products on their own computers. But to improve consistency of record-keeping across stores, the store owner now wants managers at all stores to share the same inventory of products.

As a lead developer on your team, the professor has deployed a "Products API" to a public server available at https://nyu-info-2335-products-api-csv.herokuapp.com. He explains, each store can use its own "API Client" application to issue HTTP requests to the API, and the API will perform the corresponding operations on the shared CSV inventory of products.

## Objective

Your objective is to write a command-line Python application that will allow users in any store to create, read, update, and destroy products from this shared inventory.

## Challenges

First, read the [Products API's Documentation](https://github.com/prof-rossetti/products-api-flask/tree/csv#api-documentation), which describes how to make requests to perform certain CRUD operations. You'll see some `curl` references in there, but that is a command-line utility, and there isn't actually any Python code in there. The parts of the documentation you should focus on for each operation are: "what kind of request do I need to make?" and "which URL do I make the request to?"

After consulting the docs, issue an appropriate HTTP request in Python to satisfy each of the challenges below.

### List Products

API Documentation: https://github.com/prof-rossetti/products-api-flask/tree/csv#list-products

Request information about all products, then loop through and print the "id" and "name" of each.

### Show a Product

API Documentation: https://github.com/prof-rossetti/products-api-flask/tree/csv#show-product

Choose a product identifier from the list, then request information about that specific product, then print all the product's attributes.

### Destroy a Product

API Documentation: https://github.com/prof-rossetti/products-api-flask/tree/csv#destroy-product

Request to delete the previously-selected product from the inventory.

### Create a new Product

API Documentation: https://github.com/prof-rossetti/products-api-flask/tree/csv#create-product

Request to create a new product in the inventory.

### Update a Product

API Documentation: https://github.com/prof-rossetti/products-api-flask/tree/csv#update-product

Request to update the new product you recently created.
