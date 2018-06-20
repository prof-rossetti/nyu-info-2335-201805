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

If you are struggling to identify areas of your code to test, consider thinking about questions like the following:

  + "As I was developing this application, what manual steps did I take to ensure it was functioning properly? And can I automate those manual processes?"
  + "Is it possible for the application to receive user inputs that are unexpected or invalid? And how should the application handle various invalid inputs?"
  + "How should the application's component functions perform given various inputs, whether valid or invalid?"
  + If the application processes data from the Internet: "Is there a way to test the application's functionality without making any additional network requests?" (see also: Stocks App [testing notes](/projects/stocks-app/project.md#automated-tests) and [example tests](https://github.com/s2t2/stocks-app-py-2018/blob/master/tests/adviser_test.py#L17-L24))
  + "Are there any functions or sections of the code which aren't very straightforward or easy to understand? And is there a way to use examples to communicate what is supposed to happen?"

As you document for your application, strive to make it as easy as possible for someone else (or even your future self) to install and run it, and understand what it is about.
