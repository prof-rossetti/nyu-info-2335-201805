# Python Language Overview

## The `flask` Package

Reference:

  + [Website](http://flask.pocoo.org/)
  + [Docs](http://flask.pocoo.org/docs/1.0/)
  + [Source](https://github.com/pallets/flask)
  + [Quick-start Guide](http://flask.pocoo.org/docs/1.0/quickstart/)
  + [Tutorial](http://flask.pocoo.org/docs/1.0/tutorial/)

The `flask` package provides a micro-framework for making applications with web interfaces (a.k.a "web applications").

Run a `flask` application "in development" using a web server on your local machine, and/or "in production" using a remote web server hosted by a provider like Heroku. If you run it in development, you should be able to use it by visiting `localhost:5000` in a browser, whereas if you run it in production, you should be able to use it by visiting the production server's URL.

### Installation

First install `flask`, if necessary:

```sh
# For Pipenv users (Mac or Windows), run from a project's root directory:
pipenv install flask

# For Homebrew-installed Python 3.x on Mac OS:
pip3 install flask

# All others:
pip install flask
```

### Usage

Follow the [official tutorial](http://flask.pocoo.org/docs/1.0/tutorial/).

See also these example applications by the professor:

  + [Products API (Flask)](https://github.com/prof-rossetti/products-api-flask) - just a JSON API with no front-end interface, uses CSV datastore.
  + [Salad System (Flask)](https://github.com/prof-rossetti/salad-system-flask) - includes a front-end interface, and uses an SQL datastore, although it would be possible to use a CSV datastore instead.
