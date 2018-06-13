import csv
from dotenv import load_dotenv
import json
import os
import pdb
import requests
import datetime

def parse_response(response_text):
    # response_text can be either a raw JSON string or an already-converted dictionary
    if isinstance(response_text, str): # if not yet converted, then:
        response_text = json.loads(response_text) # convert string to dictionary

    results = []
    time_series_daily = response_text["Time Series (Daily)"] #> a nested dictionary
    for trading_date in time_series_daily: # FYI: can loop through a dictionary's top-level keys/attributes
        # pdb.set_trace()

        prices = time_series_daily[trading_date] #> {'1. open': '101.0924', '2. high': '101.9500', '3. low': '100.5400', '4. close': '101.6300', '5. volume': '22165128'}
        result = {
            "date": trading_date,
            "open": prices["1. open"],
            "high": prices["2. high"],
            "low": prices["3. low"],
            "close": prices["4. close"],
            "volume": prices["5. volume"]
        }
        results.append(result)
    return results

def write_prices_to_file(prices=[], filename="datab/prices.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "open", "high", "low", "close", "volume"])
        writer.writeheader()
        for d in prices:
            row = {
                "timestamp": d["date"], # change attribute name to match project requirements
                "open": d["open"],
                "high": d["high"],
                "low": d["low"],
                "close": d["close"],
                "volume": d["volume"]
            }
            writer.writerow(row)


if __name__ == '__main__': # only execute if file invoked from the command-line, not when imported into other files, like tests

    load_dotenv() # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable

    api_key = os.environ.get("ALPHAVANTAGE_API_KEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'."

    # CAPTURE USER INPUTS (SYMBOL)

    symbol = input("Please input a stock symbol (e.g. 'NFLX'): ")

    # VALIDATE SYMBOL AND PREVENT UNECESSARY REQUESTS
    try:
        float(symbol)
        quit("CHECK YOUR SYMBOL, EXPECTING A NON-NUMERIC SYMBOL")
    except ValueError as e:
        pass


    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    print("ISSUING A REQUEST")

    response = requests.get(request_url)
    if "Error Message" in response.text:
        print("REQUEST ERROR, PLEASE TRY AGAIN.  CHECK YOUR STOCK SYMBOL.")
        quit("Stopping the program.")

    daily_prices = parse_response(response.text)

    write_prices_to_file(prices=daily_prices, filename="data/prices.csv")

    latest_closing_price = daily_prices[0]["close"]
    latest_closing_date = daily_prices[0]["date"]
    latest_closing_price = float(latest_closing_price)
    latest_closing_price_usd = "${0:,.2f}".format(latest_closing_price)

    #100 DAYS DATA
    avg_high_100days = 0
    n=0
    for i in daily_prices:
        avg_high_100days +=float(i["high"])
        n+=1
        if n ==100:
            break
    avg_high_100days = avg_high_100days/100
    avg_high_100days_usd = "${0:,.2f}".format(avg_high_100days)


    avg_low_100days = 0
    n=0
    for i in daily_prices:
        avg_low_100days +=float(i["low"])
        n+=1
        if n ==100:
            break
    avg_low_100days = avg_low_100days/100
    avg_low_100days_usd = "${0:,.2f}".format(avg_low_100days)

    #52 WEEK DATA____________________


    high=[]
    low=[]
    for n in daily_prices:
        high.append(n["high"])
    high = [float(i) for i in high]
    high52=[]
    high52 = high[0:253]
    high52_usd = max(high52)
    high52_usd1 = "${0:,.2f}".format(high52_usd)


    for n in daily_prices:
        low.append(n["low"])
    low = [float(i) for i in low]
    low52=[]
    low52 = low[0:253]
    low52_usd = min(low52)
    low52_usd1 = "${0:,.2f}".format(low52_usd)



    print("-----------------------------------------")
    print("Thanks for using robo_adviser.")
    print("The below report is procuded on: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("-----------------------------------------")
    print("The stock symbol you entered is " + symbol.upper())
    print("The Latest Closing Price for " + symbol.upper() + " on " +latest_closing_date + " is " + latest_closing_price_usd)
    print("The Recent Average High Price (100 Trading Days) is " +avg_high_100days_usd)
    print("The Recent Average Low Price (100 Trading Days) is " +avg_low_100days_usd)
    print("The 52 Week High Price is " +high52_usd1)
    print("The 52 Week Low Price is " +low52_usd1)
    print("-----------------------------------------")
    #Decision
    if avg_low_100days>low52_usd and avg_high_100days > latest_closing_price:
        print("The stock trend is Bullish, and current price is lower than Recent Average High Price, you should BUY!")
    elif avg_low_100days>low52_usd and avg_high_100days < latest_closing_price:
        print("The stock trend is Bullish, but you should wait until price dropped around Recent Average High Price to BUY!")
    else:
        print("The stock trend is Bearish, you should HOLD!")

    print("-----------DISCLAIMER---------------------")
    print("This Stock Recommendation App leveraged on resource from Alphavantage.  All Recommendation are based on Algorithm.  Please Invest Wisely.")
