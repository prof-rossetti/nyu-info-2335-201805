
import csv
import requests
from IPython import embed # I was using embed() for debugging, to try different approaches

products_csv_url = "https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201805/master/exercises/web-requests/data/products.csv"

response = requests.get(products_csv_url)
csv_string = response.text
print(response.text) #> a csv string with line break characters ("\n") and stuff
# in the past we have used the CSV module to parse files, but now we just want to parse a simple CSV string

# this code isn't what we are looking for, but it is what I tried at first...
#
# reader = csv.DictReader(csv_string)
# for row in reader:
#     print(row)
#
# it gives us a weird output like:
#> OrderedDict([('i', 'd')])
#> OrderedDict([('i', ''), (None, [''])])
#> OrderedDict([('i', 'n')])
#> OrderedDict([('i', 'a')])
#> OrderedDict([('i', 'm')])
#> OrderedDict([('i', 'e')])
# ... definitely a problem here.

# so my first google search was "python parse csv string"
# ... which led me to https://stackoverflow.com/a/42946193/670433
# ... I see some references to StringIO, but I'd rather see if there's an easier way...

# so another google search was "python dict reader csv string"
# ... which led me to https://stackoverflow.com/a/31658188/670433
# ... which mentions using .splitlines() to convert the csv string into a list of rows
# ... so I'd like to give that a try (see below)

# FYI - these answers also point us back to the CSV module docs,
# ... which provide more details and are usually worth reading:
# ...   + https://docs.python.org/3/library/csv.html#csv.reader
# ...   + https://docs.python.org/3/library/csv.html#csv.DictReader
# ...   + https://docs.python.org/3/library/csv.html#examples
# ... whenever we can get as close to the Python documentation as possible,
# ... that's our official source of information about what Python can do

# ok lets give it another try...
rows_list = csv_string.splitlines()
print(rows_list[0]) #> 'id,name,aisle,department,price'
print(rows_list[1]) #> '1,Chocolate Sandwich Cookies,cookies cakes,snacks,3.5'
# ... looking good so far

# lets try to use a DictReader to convert these to dictionaries so they are easier to process...
#
# reader = csv.DictReader(rows_list)
# for ordered_dict in reader:
#     print(ordered_dict) #> OrderedDict([('id', '20'), ('name', 'Pomegranate Cranberry & Aloe Vera Enrich Drink'), ('aisle', 'juice nectars'), ('department', 'beverages'), ('price', '4.25')])
#     print(ordered_dict["name"]) #> "Pomegranate Cranberry & Aloe Vera Enrich Drink"
#
# ... yep, that solved it!

# you'll notice we are able to reference the attributes of an OrderedDict the same way as a Dict
# ... but let's just convert the OrderedDict to a normal Dict so there are no surprises...
#
reader = csv.DictReader(rows_list)
for ordered_dict in reader:
    product = dict(ordered_dict) # conversion to a dictionary datatype
    print(product) #> {'id': '17', 'name': 'Rendered Duck Fat', 'aisle': 'poultry counter', 'department': 'meat seafood', 'price': '9.99'}
    print(ordered_dict["name"]) #> "Rendered Duck Fat"

# much better! so fun!
