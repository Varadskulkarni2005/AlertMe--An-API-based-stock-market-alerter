import os
import requests
from twilio.rest import Client
account_sid="your account id"
auth_token="c017e6165359c8c802de1c1a1639e04c"


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
sAPI_KEY="VRPNBTRECNWY1PPK"
news_api_key="591bbe1abfdd49b0841ec2e86bf909dd"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey":sAPI_KEY
}
response=requests.get(STOCK_ENDPOINT,params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_data=float(yesterday_data["4. close"])
# print(yesterday_closing_data)
#TODO 2. - Get the day before yesterday's closing stock price
day_before_data=data_list[1]
day_before_closingdata=float(day_before_data["4. close"])


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=abs(float(yesterday_closing_data-day_before_closingdata))
# print(difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent=(difference/yesterday_closing_data)*100
print(diff_percent)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent>0:
    news_params={
        "apiKey": news_api_key,
        "qInTitle":COMPANY_NAME
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles=news_response.json()["articles"]
    three_articles=articles[:3]
    print(three_articles)
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
formatted_articles=[f"Headline: {article['title']}.\nBrief : {article ['description']}" for article in three_articles]


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

client=Client(account_sid,auth_token)
for article in formatted_articles:
    message=client.messages.create(
        body=article,
        from_="+your twilio no",
        to="+91"
    )









