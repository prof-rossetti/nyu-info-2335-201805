# Application Programming Interfaces (APIs)

> Prerequisite: [Computer Networks](/notes/networks/notes.md)

Humans often interface with software manually, using a **Graphical User Interface (GUI)** which most likely includes buttons, navigation menus, drag-and-drop functionality, etc.

However, many applications also allow programmatic use. By specifying an **Application Programming Interface (API)**, or instructions on how to use the software programmatically, applications allow both humans and other applications to send data to the application and receive data from it.

It is not uncommon for a system to also use its own public API to perform its own desired functionality.

Most of todays popular APIs are **Web Services** which accept HTTP requests at specified URLs and return responses to fulfill those requests. Here are some example APIs and API providers:

 + [New York Times APIs](http://developer.nytimes.com/docs)
 + [Google APIs](https://developers.google.com/apis-explorer/#p/)
 + [Twitter APIs](https://dev.twitter.com/rest/public)
 + [Facebook Social Graph API](https://developers.facebook.com/docs/graph-api)
 + [Instagram API](https://instagram.com/developer/endpoints/)
 + [Foursquare API](https://developer.foursquare.com/docs/)
 + [GitHub API](https://developer.github.com/v3/)
 + [Yelp API](https://www.yelp.com/developers/documentation/v2/overview)
 + [Flickr API](https://www.flickr.com/services/api/)
 + [Getty Images API](http://developers.gettyimages.com/en/)
 + [US Federal Elections Commission API](https://api.open.fec.gov/developers)
 + [Alpha Vantage (Stock Market) API](https://www.alphavantage.co/documentation/)

### Authentication

Many web services require developers to first register to obtain valid credentials in the form of an **API Key** (i.e. a secret token string) and subsequently authenticate by providing the key alongside each API request. This allows the service provider to understand who is issuing each request, and can help prevent or mitigate abuse of the service.

### Response Formats

The most common format for API response data is JSON, but some APIs alternatively or additionally provide response data in XML or CSV format.

Example CSV:

```csv
city,name,league
New York,Mets,Major
New York,Yankees,Major
Boston,Red Sox,Major
Washington,Nationals,Major
New Haven,Ravens,Minor
```

Example JSON:

```js
[
  {"city": "New York", "name": "Yankees", "league":"Major"},
  {"city": "New York", "name": "Mets", "league":"Major"},
  {"city": "Boston", "name": "Red Sox", "league":"Major"},
  {"city": "Washington", "name": "Nationals", "league":"Major"},
  {"city": "New Haven", "name": "Ravens", "league":"Minor"}
]
```

Example XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<teams>
  <team>
    <city>New York</city>
    <league>Major</league>
    <name>Yankees</name>
  </team>
  <team>
    <city>New York</city>
    <league>Major</league>
    <name>Mets</name>
  </team>
  <team>
    <city>Boston</city>
    <league>Major</league>
    <name>Red Sox</name>
  </team>
  <team>
    <city>Washington</city>
    <league>Major</league>
    <name>Nationals</name>
  </team>
  <team>
    <city>New Haven</city>
    <league>Minor</league>
    <name>Ravens</name>
  </team>
</teams>
```

### Request Parameters

Many APIs allow you to specify URL parameters along with your HTTP request. These URL parameters are appended to the end of the API's base URL, starting with a single question mark (`?`) to denote the rest of the URL contains parameters. Then each parameter follows a convention where the name of the parameter is followed by an equal sign (`=`), which is followed by the desired parameter value. If there are multiple parameters, subsequent parameters after the first are separated by the ampersand character `&`.

Example request URL: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=compact&apikey=demo.

In this example, `https://www.alphavantage.co/query` is the base URL. And `function`, `symbol`, `outputsize`, and `apikey` are the names of URL parameters.

> Note: you might have to register and specify your own API key if you are seeing a message like "The demo API key is for demo purposes only."









## Representational State Transfer (REST)

Most of today's web services follow an architectural principle called "REST", which involves performing one or more operations (usually the standard CRUD operations) on one or more resources (usually records in a database).

> One of the key characteristics of a RESTful Web service is the explicit use of HTTP methods in a way that follows the protocol as defined by RFC 2616. HTTP GET, for instance, is defined as a data-producing method that's intended to be used by a client application to retrieve a resource, to fetch data from a Web server, or to execute a query with the expectation that the Web server will look for and respond with a set of matching resources.
>
> REST asks developers to use HTTP methods explicitly and in a way that's consistent with the protocol definition. This basic REST design principle establishes a one-to-one mapping between create, read, update, and delete (CRUD) operations and HTTP methods. According to this mapping:
>  + To create a resource on the server, use POST.
>  + To retrieve a resource, use GET.
>  + To change the state of a resource or to update it, use PUT.
>  + To remove or delete a resource, use DELETE.
>
> ... - [IBM website ](https://www.ibm.com/developerworks/library/ws-restful/)

When the web service accepts requests to specified URLS, each URL corresponds to a given operation and resource. For example, take these [Ruby on Rails API URL naming conventions for an example "photos" resource](http://guides.rubyonrails.org/routing.html#crud-verbs-and-actions):

HTTP Verb | Path | Controller#Action | Used for
---	| ---	| ---	| ---
GET | /photos | photos#index | display a list of all photos
GET | /photos/new | photos#new | return an HTML form for creating a new photo
POST | /photos | photos#create | create a new photo
GET	| /photos/:id | photos#show | display a specific photo
GET	| /photos/:id/edit | photos#edit | return an HTML form for editing a photo
PATCH/PUT | /photos/:id | photos#update | update a specific photo
DELETE | /photos/:id | photos#destroy | delete a specific photo

> FYI: The `:id` variable represents a given resource's unique identifier. And `Controller#Action` refers to the location and name of some function in the application's source code which performs the requested operation.
