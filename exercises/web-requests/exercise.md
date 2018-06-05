# Web Requests Exercise

> Prerequisite: [The `requests` Package](/notes/programming-languages/python/packages/requests.md)

## Objectives

This exercise asks students to use Python to process static data files located on the Internet. It focuses on "GET" requests, which are the most common and perhaps the simplest kind of HTTP request.

This exercise should help students familiarize themselves with JSON-formatted data and enhance their familiarity with CSV-formatted data.

After completing this exercise, students should be ready to issue requests to real-life web services (APIs).

## Challenges

### JSON Challenges

> HINT: the response text will be formatted as JSON, so you can use [the `json` module](/notes/programming-languages/python/modules/json.md) to parse it.

#### JSON Challenge 1 - Product

Write a Python program which issues a GET request for this JSON-formatted [product](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201805/master/exercises/web-requests/data/products/1.json) data, then print the product's "name".

> Hint: the response text will be a JSON object, like a Python dictionary.

#### JSON Challenge 2 - Products

Write a Python program which issues a GET request for this JSON-formatted [products](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201805/master/exercises/web-requests/data/products.json) data, then loop through each product and print its "name" and "id".

> Hint: the response text will be a JSON array of objects, like a Python list of dictionaries.

#### JSON Challenge 3 - Gradebook

Write a Python program which issues a GET request for this example JSON-formatted [gradebook data](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201805/master/exercises/web-requests/data/gradebook.json), then calculate and print the average, min, and max grades.

<hr>

### CSV Challenges

> HINT: the response text will be formatted as a CSV string, so you can read it using [the `csv` module](/notes/programming-languages/python/modules/csv.md).

#### CSV Challenge 1 - Products

Write a Python script which issues a GET request for this CSV-formatted [products](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201805/master/exercises/web-requests/data/products.csv), data, then loop through each product and print its "name" and "id".

#### CSV Challenge 2 - Gradebook

Write a Python program which issues a GET request for this CSV-formatted [gradebook data](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201805/master/exercises/web-requests/data/gradebook.csv), then calculate and print the average, min, and max grades.
