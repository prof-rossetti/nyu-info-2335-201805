# Servers

> Prerequisites: [Software Distribution](/notes/software/notes.md#delivery) and [Computer Networks](/notes/networks/notes.md)

Today's software services are powered by scores of keyboard-less, mouse-less, monitor-less computers called **servers**, which generally run all day or at scheduled or ad-hoc intervals.

Most servers are operated "in the cloud" by providers like [Amazon Web Services](https://aws.amazon.com/) and [Heroku](https://www.heroku.com/). These "remote servers" provide business advantages at least in terms of:

  + Cost
  + Scalability
  + Efficiency
  + Security
  + Usability
  + Reliability

Different kinds of servers perform different functions. Common server types include:

  + Application Servers
  + Database Servers
  + Email Servers
  + Web Servers

### Application Servers

To "deploy" an application to a server is to copy its source code onto the server. Once the application's source code exists on a server, the server is capable of running the software in a similar way as it would be run on a developer's local machine.

#### Deployment Environments

Name | Description | Common Developer Tasks | Primary Audience | Level of Risk
--- | --- | --- | --- | ---
Development | A computer, often a personal computer, on which you produce, develop, and test an application's source code. | Running a local web server, editing code in a text-editor, and running tests. | One or more individual members of the software development team. | Low
Staging | A computer, often a remote server, onto which you deploy an application's source code to emulate as best as possible the production environment to get a sense for how code changes will affect the application running on the production environment. | Performing usability tests, monitoring server scalability and performance. | One or more collective members of the software development team. | Medium
Production | A computer, often a remote server, onto which you deploy your application's source code for "live" usage. | Monitoring server logs. | Users, customers, and the public at large. | Very High
