# Professor Rossetti's Mac Terminal Configuration

These are some of the professor's own terminal configurations. Feel free but not obligated to use any or all of them.

## Theme

[Download](http://ethanschoonover.com/solarized/files/solarized.zip) the [Solarized](http://ethanschoonover.com/solarized) color themes, and unzip.

In Terminal Settings, import a new Profile, and choose the **solaraized/osx-terminal.app-colors-solarized/Solarized Dark ansi.terminal** theme.

Set the Solarized Dark profile theme as default.

Increase font size to 18.

## Shortcuts

Add the following contents to a special file called *~/.bash_profile*:

``` sh
# ~/.bash_profile

#
# CONFIGURATION
#

export PS1=" --->> " # see: https://www.gnu.org/software/bash/manual/html_node/Controlling-the-Prompt.html
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

#
# SHORTCUTS
#

alias ll="ls -lahG"

alias gb="git branch"
alias gd="git diff"
alias gl="git log"
alias glt="git log --graph --decorate --oneline --full-history --all --simplify-by-decoration"
alias glsd="git ls-files --deleted"
alias gpom="git pull origin master"
alias gr="git remote -v"
alias gs="git status"
```
