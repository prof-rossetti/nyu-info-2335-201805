# Stock Recommendation App

> Prerequisites: [Web Requests Exercise](/exercises/web-requests/exercise.md), [Environment Variables](/notes/software/environment-variables.md), [Package Management](/notes/programming-languages/python/package-management.md)

Assume you own and operate a financial planning business which helps customers make investment decisions.

Your objective is to build yourself a tool to automate the process of providing your clients with stock trading recommendations.

Specifically, the system should accept one or more stock or cryptocurrency symbols as information inputs, then it should request real live historical trading data from the Internet, and finally it should provide a recommendation as to whether or not the client should purchase the given stocks or cryptocurrencies.

## Requirements

### Repository Requirements

Your repository should contain files at the following locations:

   + A `README.md` file
   + A `requirements.txt` file
   + An `app` directory with a `robo_adviser.py` script inside (i.e. `app/robo_adviser.py`)
   + A `data` directory

The contents of the `requirements.txt` file should include all the packages your program requires, for example:

    ipython
    pytest
    python-dotenv
    requests

The contents of the `README.md` file should provide instructions on how someone can install, setup, and run your program. This includes instructions on how to install the required packages using Pip and/or Pipenv (e.g. a command like `pip install -r requirements.txt`). It should also describe expectations for an environment variable named `ALPHAVANTAGE_API_KEY` (see "Security Requirements" section below), and should provide instructions on how to set this variable.

### Security Requirements

Your program will need an API Key to issue requests to the [AlphaVantage API](https://www.alphavantage.co). But the program's source code should absolutely not include your API Key in it.

Instead you should set an environment variable called `ALPHAVANTAGE_API_KEY`, and your program should read your API Key from this environment variable at run-time.

You are encouraged to use a "dotenv" approach to setting project-specific environment variables by using a `.env` file in conjunction with [the `dotenv` package](/notes/programming-languages/python/packages/dotenv.md). If you do, the `.env` file should absolutely not be tracked in version control or included in your GitHub repository. HINT: you may need to use a [local `.gitignore` file](https://help.github.com/articles/ignoring-files/#create-a-local-gitignore), or just don't upload the `.env` file to GitHub.

### Functionality Requirements

Your project should adhere to the following functionality requirements, as detailed in the sections below:

  + Information Input Requirements
  + Validation Requirements
  + Information Output Requirements
  + Calculation Requirements

#### Information Input Requirements

The system should prompt the user to input one or more stock symbols (e.g. `"MSFT"`, `"AAPL"`, etc.). It may optionally allow the user to specify multiple symbols, either one-by-one or all at the same time (e.g. `"MSFT, AAPL, GOOG, AMZN"`). It may also optionally prompt the user to specify additional inputs such as risk tolerance and/or other trading preferences, as desired and applicable.

#### Validation Requirements

Before requesting data from the Internet, the system should first perform preliminary validations on user inputs. For example, it should ensure stock symbols are a reasonable amount of characters in length and not numeric in nature.

If preliminary validations are not satisfied, the system should display a friendly error message like "Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again." and stop execution.

Otherwise, if preliminary validations are satisfied, the system should proceed to issue a GET request to the [AlphaVantage API](https://www.alphavantage.co/documentation/) to retrieve corresponding stock market data.

When the system makes an HTTP request for that stock symbol's trading data, if the stock symbol is not found or if there is an error message returned by the API server, the system should display a friendly error message like "Sorry, couldn't find any trading data for that stock symbol", and it should stop program execution, optionally prompting the user to try again.

#### Information Output Requirements

After receiving a successful API response, the system should write historical stock prices to one or more CSV files located in the repository's `data` directory. The CSV file contents should resemble the following example:

    timestamp, open, high, low, close, volume
    2018-06-04, 101.2600, 101.8600, 100.8510, 101.6700, 27172988
    2018-06-01, 99.2798, 100.8600, 99.1700, 100.7900, 28655624
    2018-05-31, 99.2900, 99.9900, 98.6100, 98.8400, 34140891
    2018-05-30, 98.3100, 99.2500, 97.9100, 98.9500, 22158528

If the system processes only a single stock symbol at a time, the system may use a single CSV file named something like `data/prices.csv`. Whereas if the system processes multiple stock symbols at a time, for each stock symbol, the system should write historical trading data to a corresponding CSV file that is named after the stock symbol (e.g. `data/prices_msft.csv`, `prices_aapl.csv`, etc.). If writing multiple CSV files, the program should have a way of cleaning-up to prevent uncontrolled proliferation of new files.

After writing historical data to a CSV file, the system should perform calculations (see "Calculation Requirements" section below) to produce the following outputs:

  + The **selected stock symbol(s)** (e.g. "Stock: MSFT")
  + The **date and time when the program was executed**, formatted in a human-friendly way (e.g. "Run at: 11:52pm on June 5th, 2018")
  + The **date when the data was last refreshed**, usually the same as the latest available day of daily trading data (e.g. "Latest Data from: June 4th, 2018")
  + For each stock symbol: its **latest closing price**, its **recent average high price**, and its **recent average low price**, calculated according to the instructions below, and formatted as currency with a dollar sign and two decimal places and a thousands separator as applicable (e.g. "26-week high: $1,234.56", etc.)
  + A **recommendation** as to whether or not the client should buy the stock (see guidance below), and optionally what quantity to purchase. The nature of the recommendation for each symbol can be binary (e.g. "Buy" or "No Buy"), qualitative (e.g. a "Low", "Medium", or "High" level of confidence), or quantitative (i.e. some numeric rating scale).
  + A **recommendation explanation**, describing in a human-friendly way the reason why the program produced the recommendation it did (e.g. "because the stock's latest closing price is exceeds threshold XYZ")

#### Calculation Requirements

The **latest closing price** should be equal to the stock's "close" price on the latest available day of trading data.

The **recent average high price** should be equal to the maximum daily "high" price, for all available days in approximately the past 100 available days of trading data.

The **recent average low price** should be calculated in a similar manner as the **recent average high price**, but it should instead be equal to the minimum of all daily "low" prices.

> NOTE: By default, the [daily data returned by the AlphaVantage API](https://www.alphavantage.co/documentation/#daily) uses an `outputsize` parameter value of `compact`. This "compact" response should provide daily data covering the previous 100 trading days, which is sufficient to use to calculate the **recent average high** and **recent average low** prices. It is acceptable and recommended to use these default, "compact" responses to calculate these recent average prices.

You are free to develop your own custom **recommendation** algorithm. This is perhaps one of the most fun and creative parts of this project. :smiley: One simple example algorithm would be (in pseudocode): If the stock's latest closing price is less than 20% above its 52-week low, "Buy", else "Don't Buy".

#### Further Exploration

##### 52-Week Highs and Lows

For students desiring optional further exploration, instead of calculating and printing the stock's **recent average high** and **recent average low**, calculate and print the stock's **52-week high** and **52-week low**, respectively.

The **52-week high** should be equal to the maximum "high" price, for each available day in approximately the past year. For example, if the last available day of trading data is June 1st, 2018, the program should find the maximum price of all the available "high" prices between around June 1st, 2017 and June 1st, 2018.

The **52-week low** should be calculated in a similar manner as the 52-week high, but it should instead be equal to the minimum of all "low" prices within the past year.

> HINT: If you were previously requesting daily data, you will have to change your approach to either request more of it (i.e. by requesting a "full" response by specifying the URL parameter `&outputsize=full`), or to instead request weekly data. Theoretically the maximum weekly "high" price should be the same as the maximum daily "high" price within the same period.

> NOTE: If you do request "full" responses of daily data, the size of the response may drastically increase, and the speed of your requests may slow down noticeably. If you think these changes negatively impact user experience, you might want to consider requesting weekly data instead.

##### Automated Tests

For students desiring optional further exploration, the repository should contain meaningful and relevant tests. If there are any tests, they should exist in a "tests" directory in a file called something like `robo_adviser_test.py` (e.g. `tests/robo_adviser_test.py`).

One best practice when testing applications that issue HTTP requests is to avoid issuing any requests during automated testing. To test your application's ability to parse API responses without actually issuing a request, use an example "mock" response instead. For example you may save a copy of a real response into a file named something like `tests/example_responses/daily_response.json`. Then configure your tests to read its inputs from this local file instead of reading the response that would have been returned by the API.

If you would like clarification about recommended testing strategies or general advice on how to meaningfully test this application, ask the professor, who would be happy to help.





























## Submission Instructions

By this time, students should be able to replicate the submission instructions from previous deliverables, also abbreviated below.

### Step 1 - Creating a new Project Repo

Either "fork" the [Starter App](https://github.com/prof-rossetti/stocks-app-py) and build on-top of it, or create your own repository from scratch.

If creating a repository from scratch,
use the GitHub.com online interface to create a new GitHub repository under your control
named something like "stocks-app".
When you create the new repository, in order to easily use the GitHub.com online interface to manage files,
check the box to **Initialize this repository with a README**.
Once the repository is created, add all the necessary files and commit them.
At this time you should be able to view your files online at your project repository's URL.

### Step 2 - Forking the Course Repo

If you have not yet already forked the course repository, do so now.

Otherwise, if you have already forked the course repository
(i.e. if you have already submitted a previous exercise),
then you will need to update your existing fork instead.

### Step 3 - Submitting a Pull Request

Add a new record to the [submissions file](submissions.csv),
to include your GitHub username and the repository's URL (e.g. `https://github.com/YOUR_USERNAME/stocks-app`).
After updating your own fork, you will need to submit a Pull Request
for your content to be accepted into the main course repository. Before you update your fork, make sure you don't have any outstanding [pull requests](https://github.com/prof-rossetti/nyu-info-2335-201805/pulls).

## Evaluation

Submissions will be evaluated based on ability to meet each of the component requirements (see corresponding sections above for detailed instructions):

Category | Weight
--- | ---
Repository Requirements | 10%
Security Requirements | 15%
Information	Input Requirements | 10%
Validation Requirements | 25%
Information	Output Requirements | 20%
Calculation Requirements | 20%

This rubric is tentative, and may be subject to slight adjustments during the grading process.

The professor reserves the right to award up to 10% extra credit for presence of meaningful automated tests (see "Further Exploration" above)!
