import requests
import json

url = "https://data.cityofnewyork.us/api/views/gra9-xbjk/rows.json?accessType=DOWNLOAD"
req_url = requests.get(url)
# print(req_url.status_code)

if req_url.ok:
    # print(req_url.text)
    # for a in req_url.text:
        # print(a)
    formatted_data = json.loads(req_url.text)
    print(formatted_data["data"])

restaurant_data = formatted_data["data"]
for a in restaurant_data:
    if a[17] is not "A":
        print(a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[17])
        print()


def sort_by_zip():
    pass

product_id = input("Hey, what's the identifiers of the product you want to display: ")
matching_products = [p for p in products if int(p["id"]) == int(product_id)]
matching_product = matching_products[0]
del products[products.index(matching_product)]
