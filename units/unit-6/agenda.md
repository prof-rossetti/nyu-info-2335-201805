# Unit 6 Agenda

## Objectives

Learn how to use Python to process data from the Internet, focusing on JSON-formatted data returned by APIs.

## Discussions and Notes

At your own pace, familiarize yourself with these written materials:

  + [Computer Networks, the Internet, and HTTP](/notes/networks/notes.md) <-- focus here
  + [Application Programming Interfaces (APIs)](/notes/software/apis.md) <-- focus here
  + [Environment Variables](/notes/software/environment-variables.md) <-- focus here
  + Python Programming Language:
     + [The `json` Module](/notes/programming-languages/python/modules/json.md), revisited
     + [The `os` Module](/notes/programming-languages/python/modules/os.md#accessing-environment-variables), revisited
  + Third-party Python Packages:
     + [The `requests` Package](/notes/programming-languages/python/packages/requests.md) <-- focus here
     + [The `dotenv` Package](/notes/programming-languages/python/packages/dotenv.md)
     + [The `BeautifulSoup` Package](/notes/programming-languages/python/packages/beautifulsoup.md) <-- optional further exploration, only if you are familiar with HTML, and recognizing there will be an opportunity later in the semester to explore this package further

Spend at most around 30 minutes on these materials.

## Ungraded Exercises

When you are ready to practice issuing HTTP requests to get data, start with the Web Requests Exercise. If you are making good time, you might try moving on to API Client Exercise, but if you are short on time, you might want to consider trying it out sometime after class.

  + [Web Requests](/exercises/web-requests/exercise.md) <-- do all of the JSON challenges. if you're struggling with them, ask for help right away. feel free to skip the CSV challenges and return to them later
  + [API Client](/exercises/api-client/exercise.md) <-- a little harder, but definitely very fun, especially when you start creating and deleting products and seeing the products other people have created

Spend at most around 60 minutes working through one or both of these exercises.

## Projects

With at least 75-90 minutes of remaining class time, move on to set up and start developing your Stock Recommendation App. If using a starter repo with existing code is helpful for you, consider adapting your own solution from this [Starter Repo](https://github.com/prof-rossetti/stocks-app-py), otherwise feel free to start from scratch.

  + [Stock Recommendation App](/projects/stocks-app/project.md)

Before you start requesting stock data, you will need to [obtain an AlphaVantage API Key](https://www.alphavantage.co/support/#api-key), and you should consider spending a few minutes to consult the [AlphaVantage API Documentation](https://www.alphavantage.co/documentation/) to learn about which requests are available.

**Your mission by the end of class** is to develop your Stock Recommendation App to:

   1. Prompt a user to input a stock symbol,
   2. Issue a "GET" request to the AlphaVantage API to get that symbol's historical trading data, and
   3. Parse the JSON response and traverse its nested structure to find and print the stock's "latest closing price"
