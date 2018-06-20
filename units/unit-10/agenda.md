# Unit 10 Agenda

duration (mins) | usage
--- | ---
60 | Deploying to Production Exercise (optional)
120 | Freestyle Project Development and Testing

## Discussion and Notes

  + [Hardware](/notes/hardware/notes.md) and [Servers](/notes/hardware/servers.md)
  + [Heroku](/notes/hardware/heroku.md) and the `heroku` command-line utility (optional further exploration)

## Exercises

  + [Deploying to Production](/exercises/deploying-to-production/exercise.md) (optional further exploration :smiley_cat:)

## Projects

+ [Self-directed (a.k.a. "Freestyle") Project](/projects/freestyle/project.md) - Implementation Phase

As you finish developing your app, take some time to ensure it is well tested and documented.

As you think about ways to **test** your application, consider asking yourself questions like the following:

  + *As I was developing this application, what manual steps did I take to ensure it was functioning properly? Can I automate those manual processes?*
  + *Is it possible for the application to receive user inputs that are unexpected or invalid? How should the application handle various invalid inputs?*
  + *How should the application's component functions perform given various inputs, whether valid or invalid?*
  + *Are there any functions or sections of the code which aren't easy to read or understand? Is there a way to use examples to communicate what is supposed to happen?*
  + If the application processes data from the Internet: *Is there a way to test the application's functionality without making any additional network requests?* (see also: Stocks App [testing notes](/projects/stocks-app/project.md#automated-tests) and [example tests](https://github.com/s2t2/stocks-app-py-2018/blob/master/tests/adviser_test.py#L17-L24))
  + If the application processes data from a CSV file or database: *Is there a way to test the application's functionality without affecting the development environment datastore?* (see also: Inventory Mgmt App [example tests](https://github.com/s2t2/python-csv-crud-app/blob/edd157c7f26b81389f8fadb3d2c5ad7fd4732466/tests/test_crud_app.py#L9-L12))

As you **document** for your application, strive to make it as easy as possible for someone else (or even your future self) to install it, use it, and understand what it is about.
