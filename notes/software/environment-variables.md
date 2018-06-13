# Environment Variables

**Environment variables** allow developers to customize the environment in which an application is operating.









## Setting

Environment variables can be set "globally", in which case they are accessible by any program running on that given computer. Or they can be set "locally", in which case they are only accessible by programs located in a specific directory.

After setting an environment variable using one of the approaches below, reference the section on "Getting" to see if the variable was set properly.

### Setting on Mac

Mac users should be able to manage global environment variables using a hidden file called
`~/.bash_profile`. Open the file with your text editor (e.g. `atom ~/.bash_profile`), and place inside the following contents:

```sh
# ~/.bash_profile
export NYU_INFO_2335="SecretPassword123"
```

Then exit and re-open your Terminal for the changes to take effect.

### Setting on Windows

Windows users can set local environment variables from the command-line using the `set` keyword:

```sh
# Windows Command Prompt:
set NYU_INFO_2335="SecretPassword123"
```

> NOTE: if you close your command prompt and re-open it, you will need to re-set the environment variable.

### Setting Locally Using Dotenv File

To set project-specific local environment variables on either Mac or Windows, consider using the "dotenv" approach. Create a special file in your project named `.env` and place inside content like the following:

```sh
# my-project/.env
NYU_INFO_2335="SecretPassword123"
```

To load these `.env` variables into a Python program, use [the `dotenv` package](/notes/programming-languages/python/packages/dotenv.md).

> NOTE: Some students have [reported](https://github.com/prof-rossetti/nyu-info-2335-201805/issues/157) the "dotenv" approach does not work for them. If the "dotenv" approach does not work for you, no worries, just stick to one of the other operating system-specific approaches described above.

















## Getting

You will know you have successfully set an environment variable when you can access its value from the command-line:

```shell
# Mac Terminal:
echo $NYU_INFO_2335 #> SecretPassword123

# Windows Command Prompt:
echo %NYU_INFO_2335% #> SecretPassword123
```

To access environment variables from within a Python program, use [the `os` module](/notes/programming-languages/python/modules/os.md#accessing-environment-variables).
















<hr>


## Benefits

### Security

Sometimes applications need to reference secret passwords, tokens, and other values. This is especially the case when the app is authenticating to some other service on behalf of a given user.

But hard-coding these sensitive values into a program's source code would be irresponsible from a security standpoint, especially when sharing the source code online. You don't want your passwords on GitHub for everyone to see.

Environment variables provide a way of separating these secret values from a program's source code.

### Collaboration and Customization

Sometimes developers need to run an application in different environments. For example, two developers may want to use the same program to download their respective social media posts from an API.

But each developer has their own private API key which provides access to their own private social media posts. It would be ineffective for them to use the exact same source code, and inefficient to maintain two slightly different versions of the application's source code.

Environment variables allow developers to share the same source code while specifying different values at run-time.

### Testing and Delivery

Environment variables allow developers to specify customized environments in which to develop, test and deliver their application.

Environment variable customization allows an application to perform differently in a "test" environment than it would in a user-facing "production" environment. For example, developers can use the application to manipulate example data in a "test" environment without affecting real user data in the "production" environment.
