# Git Command-line Utility (CLI)

References:

  + https://education.github.com/git-cheat-sheet-education.pdf
  + https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf
  + https://www.git-tower.com/blog/git-cheat-sheet/
  + https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line

## Installation

### Installation on Mac

First see if Git is already installed (it may come pre-installed):

```sh
# Mac Terminal:
which git
git --version
```

If these commands produce a filepath-looking output and version-looking output, respectively, then Git is already installed. Nice! You can skip down to the "Git Commands Overview" section.

Otherwise, if Git is not already installed, or if you would prefer to use a Homebrew-installed version, you are recommended to use Homebrew to install Git:

```sh
# Mac Terminal:
brew install git
```

### Installation on Windows

Try downloading [Git for Windows](https://gitforwindows.org/) and following the installation instructions. This software includes both a Git Bash command-line application and a Git GUI application. The Git Bash application is where you can execute Git commands.

## Git Commands Overview

> NOTE: after executing some commands like `git log` and `git diff`, you can press the "Enter" key to keep reading, and type "q" to quit when you are done.

> NOTE: after executing other commands like `git pull`, you may find yourself at times in an unfamiliar-looking "Vi" text editor window, which you can exit by pressing the "shift + ZZ" keys.

### Initializing a Local Repository

Navigate into a project directory, then initialize a new repository there:

```sh
cd path/to/my/project # where path/to/my/project is the actual path to your project directory
git init . # initialize a new git repository, creating a hidden folder called .git in your project's root directory
```

### Viewing Revision History

List the most recent revisions:

```sh
git log
```

Show details about the most recent revision:

```sh
git show # optionally specify any commit's identifier, or "SHA", to show that specific commit
```

> NOTE: for newly-created repositories, there won't be any revisions.

### Making Revisions

Use your text editor to add, delete, and/or modify files, and save them as appropriate.

### Committing Changes

After making and saving changes, detect and review them:

```sh
git status # see which files have changed since the last commit
git diff # see how those files have changed (only shows diffs for files that existed during the last version, not for newly created files)
```

After reviewing the changes, stage and commit changes:

```sh
git add . # this "stages" the files for commit. you can undo this with `git reset`. use the period (`.`) to add all changed files in the repository, or specify a single filename to add only that file
git commit -m "my message" # saves the changes and adds a unique reference identifier for this particular version
```

Repeat this process of reviewing and committing revisions as necessary as you iteratively develop your software.

### Cloning Remote Repositories

If there is a remote repository you would like to download, clone it:

```sh
git clone REMOTE_ADDRESS # to find the REMOTE_ADDRESS, visit a repo's homepage on GitHub and click the big green button on the right side that says "Clone or download". The address should resemble https://github.com/USERNAME/REPONAME.git (HTTPS), or `git@github.com:USERNAME/REPONAME.git` (SSH)
```

After cloning, a default remote address named "origin" is automatically created. You can check a local repository's remote addresses at any time:

```sh
git remote -v
```

### Managing Remote Addresses

If you would like to upload the contents of a local repository to a remote address, follow these steps in order:

  1. Assuming you don't already have a remote repo, create a new repo on GitHub, then note its remote address. Sometimes when you create a new empty repo on GitHub, it will display a screen that contains the `REMOTE_ADDRESS`. Otherwise, to find the `REMOTE_ADDRESS` of any existing GitHub repository, visit its homepage and click the big green "Clone or download" button. The address should resemble `https://github.com/USERNAME/REPONAME.git` (HTTPS), or `git@github.com:USERNAME/REPONAME.git` (SSH)
  2. From the command-line, navigate to the root directory of your existing local repository (e.g `cd path/to/my-dir`).
  3. Configure a "remote" address for your local repository: `git remote add origin REMOTE_ADDRESS`. NOTE: the overwhelming convention is to name your default GitHub remote address "origin".
  4. Associate the local repo with the remote repo (one-time, first-time only): `git pull origin master --allow-unrelated-histories`. After doing so, you may be in a "Vi" text editor window, which you can exit by pressing the "shift + ZZ" keys.

### Syncing Local and Remote Repositories

Assuming you have already associated a local repository with a remote repository named "origin":

```sh
git pull origin master # download recent contents from remote repo, in case changes have been made to the remote repository since you last pushed.
git push origin master # upload local repo contents to remote address
```

Sometimes after pulling, you may see merge conflicts, in which case you might need to perform a "rebase" before being able to push. The rebase process can be difficult, so don't hesitate to ask the professor for help.

After pushing successfully, you should be able to visit your remote repository on GitHub and see your code there.
