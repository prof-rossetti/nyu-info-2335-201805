# Development Process Notes

Setup the directory/repository structure:

```sh
cd ~/Desktop
mkdir my-stocks-app
cd my-stocks-app
mkdir app
touch app/robo_adviser.py
```

Set up a virtual environment and install packages:

```sh
pipenv install
pipenv install requests
pipenv install python-dotenv
pipenv install ipython
```

Run the script:

```sh
pipenv shell
(my-stocks-app-abc123) bash-3.2$ python app/robo_adviser.py
```
