# CSV Processing Exercise

## Objectives

This exercise provides a practical business-related opportunity to practice using Python to process CSV files.

## Instructions

Assume you own an online retail business which sells its products through an online marketplace. At the end of each month, the online marketplace provides you with a raw CSV file representing all sales for that month. Here are some example files:

   + [`sales-201710.csv`](data/sales-201710.csv)
   + [`sales-201711.csv`](data/sales-201711.csv)
   + [`sales-201712.csv`](data/sales-201712.csv)
   + [`sales-201801.csv`](data/sales-201801.csv)
   + [`sales-201802.csv`](data/sales-201802.csv)
   + [`sales-201803.csv`](data/sales-201803.csv)

The expected name for any of these files resembles "sales-`YYYYMM`.csv", where `YYYY` represents the year and `MM` represents the month number. The expected CSV headers for any of these files are: `date`, `product`, `unit price`, `units sold`, and `sales price`, in that order, assumed to exist on the very first row in the CSV file.

Write a Python script which automates the process of transforming this monthly sales data into a report of business insights.

Your submission should loop through each of the provided CSV files, and for each print the following information outputs:

  1. The name of the year and month, formatted in a human-friendly way (e.g. "Sales Report for March, 2018")
  2. Total monthly sales, equivalent to the sum of total monthly sales for each product, formatted as USD with a dollar sign and two decimal places (e.g. "Total Monthly Sales: $12,000.71").
  3. A list of the top five selling products, and total monthly sales for each, formatted as USD with a dollar sign and two decimal places (e.g. "1) Button-Down Shirt: $6,960.35", "2) Super Soft Hoodie: $1,875.00", etc.).

### Setup

To setup this exercise, either "fork" and download this [Starter Repo](https://github.com/prof-rossetti/monthly-sales-reporting-py), or follow the instructions below.

Create a new directory on your Desktop called something like "csv-processing", then navigate there from the command-line.

Within that directory, create a new directory called "data" and place inside it all of the provided CSV files (e.g. `data/sales-201803.csv`, etc.). HINT: you could either copy and paste the "raw" file contents, or you could download the files and move them into the proper directory.

Also create a new file called `sales_report.py` and place inside the following code:

```python
# sales_report.py

print("PROCESSING SOME CSV FILES HERE")

# TODO: write some Python code to produce the desired output
```

Run the script to see it print:

```sh
# For Homebrew-installed Python 3.x on Mac OS:
python3 sales_report.py

# All others:
python sales_report.py
```

Great, now you are ready to start the exercise.

## Submission Instructions

> Submission of this exercise is optional. The professor may announce conditions under which a full working solution will earn extra credit to be applied toward the final exam. By this time, students should be able to replicate the submission instructions for previous deliverables, also abbreviated below.

### Step 1 - Creating a new Project Repo

Use the GitHub.com online interface to create a new GitHub repository under your control
named something like "csv-processing".
When you create a new repository, in order to easily use the GitHub.com online interface to manage files,
check the box to **Initialize this repository with a README**.
Once the repository is created, add a file to it called `sales_report.py`.
Paste your Python code into that file, then save and commit it. Revise this file until it produces the desired outputs.
At this time you should be able to view your file online at your project repository's URL.

### Step 2 - Forking the Course Repo

If you have not yet already forked the course repository, do so now.

Otherwise, if you have already forked the course repository
(i.e. if you have already submitted a previous exercise),
then you will need to update your existing fork instead.
To do this from the GitHub.com online interface, delete your fork from the repository's "Settings" menu, then re-fork it. There are easier ways to do this from the command-line, but we will get to that later.

### Step 3 - Submitting a Pull Request

Add a new record to the [submissions file](submissions.csv),
to include your GitHub username and the repository's URL (e.g. `https://github.com/YOUR_USERNAME/csv-processing`).
Finally, submit a Pull Request
for your content to be accepted into the main course repository.
