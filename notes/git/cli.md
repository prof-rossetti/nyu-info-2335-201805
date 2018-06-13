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
which git #> /usr/local/bin/git
git --version #> git version 2.10.0
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

### Local Repositories

#### Initializing a Local Repository

Navigate into a project directory, then initialize a new repository there:

```sh
cd path/to/my/project # where path/to/my/project is the actual path to your project directory
git init . # initialize a new git repository, creating a hidden folder called .git in your project's root directory
```

#### Viewing Revision History

> NOTE: newly-created repositories won't have any revisions to view until you make your first commit (see "Committing Changes" below)

List the most recent revisions:

```sh
git log
```

Show details about the most recent revision:

```sh
git show # optionally specify any commit's identifier, or "SHA", to show that specific commit (e.g. `git show a5290eda34e9e0d89b90ae1cc01afe7753c294b8`)
```

#### Making Revisions

Use your text editor to add, delete, and/or modify files, then save them.

#### Committing Changes

After making and saving changes, detect and review them:

```sh
git status # see which files have changed since the last commit
git diff # see how those files have changed (only shows diffs for files that existed during the last version, not for newly created files)
```

After reviewing the changes, if you are satisfied, stage and commit them:

```sh
git add . # this "stages" the files for commit. specify a period (`.`) to add all changed files, or specify a single filename to add only that file (e.g. `git add path/to/file.py`)
git commit -m "my message" # saves the changes and adds a unique reference identifier for this particular version
```

Continue to iteratively repeat the process of reviewing and committing revisions as you incrementally develop your software.

#### Reverting Changes

One of the biggest benefits of version control is the ability to revert to previous versions. If you need to restore the state of your repository to some previous commit:

```sh
git reset --hard abc123def456 # where abc123def456 is the identifier, or "SHA", of the commit you would like to revert to
```








### Remote Repositories

When you create a new empty repository on GitHub, it will display a screen that contains the `REMOTE_ADDRESS`. Otherwise, to find the `REMOTE_ADDRESS` of any existing GitHub repository, visit its homepage and click the big green "Clone or download" button. The address should resemble `https://github.com/USERNAME/REPONAME.git` (HTTPS), or `git@github.com:USERNAME/REPONAME.git` (SSH).

#### Cloning Remote Repositories

If there is a remote repository you would like to download, clone it (where `REMOTE_ADDRESS` refers to the repository's remote address):

```sh
git clone REMOTE_ADDRESS
```

After cloning, a default remote address named "origin" is automatically created. You can check a local repository's remote addresses at any time:

```sh
git remote -v
```

#### Managing Remote Addresses

Add or remove a local repository's remote addresses, where `REMOTE_NAME` refers to the name of the remote address, (e.g. "origin"), and `REMOTE_ADDRESS` refers to the repository's remote address:

```sh
git remote add REMOTE_NAME REMOTE_ADDRESS
git remote rm REMOTE_NAME REMOTE_ADDRESS
```

If you would like to upload the contents of a local repository to a remote address but you don't already have a remote repo, follow these steps in order:

  1. Create a new repo on GitHub, then note its remote address.
  2. From the command-line, navigate to the root directory of your existing local repository (e.g `cd path/to/my-dir`).
  3. Configure a "remote" address for your local repository: `git remote add origin REMOTE_ADDRESS`. NOTE: the overwhelming convention is to name your default GitHub remote address "origin".
  4. Associate the local repo with the remote repo (one-time, first-time only): `git pull origin master --allow-unrelated-histories`. After doing so, you may be in a "Vi" text editor window, which you can exit by pressing the "shift + ZZ" keys.
  5. Follow the "Syncing Local and Remote Repositories" section, below, to push your local changes up to GitHub.

#### Syncing Local and Remote Repositories

Assuming you have already associated a local repository with a remote address named "origin":

```sh
git pull origin master # downloads recent contents from the remote repo, in case changes have been made to the remote repo since you last pushed.
git push origin master # uploads local repo contents to remote address
```

Sometimes after pulling, you may see merge conflicts, in which case you might need to perform a "rebase" before being able to push. The rebase process can be difficult, so don't hesitate to ask the professor for help.

After pushing successfully, you should be able to visit your remote repository on GitHub and see your code there.
