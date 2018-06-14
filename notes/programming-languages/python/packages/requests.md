# Python Language Overview

## The `requests` Package

> Prerequisite: [Computer Networks](/notes/networks/notes.md) and [APIs](/notes/software/apis.md)

The `requests` package provides an easy way for Python programs to issue HTTP requests, whether scraping the contents of a web page, or exchanging data with an API.

Reference: http://docs.python-requests.org/en/master/.

### Installation

First install the package, if necessary:

```` sh
# For Pipenv users (Mac or Windows), run from a project's root directory:
pipenv install requests

# For Homebrew-installed Python 3.x on Mac OS:
pip3 install requests

# All others:
pip install requests
````

### Usage

#### Issuing HTTP Requests

Issue a "GET" request (perhaps the most common):

```py
import requests

request_url = "https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201805/master/exercises/web-requests/data/products/1.json"
response = requests.get(request_url)
print(response.status_code)
print(response.text)
```

> NOTE: if you are looking for more example URLs to request data from, head on over to the [Web Requests Exercise](/exercises/web-requests/exercise.md).

In addition to "GET" requests, you can also issue other types of requests like "POST", "PUT", and "DELETE", sending data to the server as necessary:

```py
my_data = {} # a dictionary representing the data you want to send to the server

request_url = "https://example-api.com/some/path" # <--- replace with a real url that accepts POST requests
response = requests.post(request_url, json=my_data) # where you can pass a dictionary as the `json` parameter
print(response.status_code)

request_url = "https://example-api.com/some/path" # <--- replace with a real url that accepts PUT requests
response = requests.put(request_url, json=my_data) # where you can pass a dictionary as the `json` parameter
print(response.status_code)

request_url = "https://example-api.com/some/path" # <--- replace with a real url that accepts DELETE requests
response = requests.delete(request_url)
print(response.status_code)
```

> NOTE: if you are looking to try out these other kinds of requests, head on over to the [API Client Exercise](/exercises/api-client/exercise.md), which links to documentation for the "Products API", which provides example URLs you can use.

### Parsing HTTP Responses

If the response contains JSON, you can use [the `json` module](/notes/programming-languages/python/modules/json.md) to parse it:

```py
response = requests.get(some_url)
response_data = json.loads(response.text)
print(type(response_data)) #> <class 'list'> or <class 'dict'>
```

If the response contains HTML, you can use [the `BeautifulSoup` package](/notes/programming-languages/python/packages/beautifulsoup.md) to parse it.
