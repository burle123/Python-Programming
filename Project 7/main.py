import requests
import json

query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/top-headlines?q={query}&apiKey=dbe57b028aeb41e285a226a94865f7a7"

r = requests.get(url)
news = json.loads(r.text)

# Print the entire response for debugging
print(news, type(news))

# Check if the request was successful
if news.get("status") != "ok":
    print("Error fetching news:", news.get("message"))
else:
    # Check if "articles" key exists
    if "articles" in news and len(news["articles"]) > 0:
        for article in news["articles"]:
            print(article.get("title"))
            print(article.get("description"))
            print("--------------------------------------")
    else:
        print("No news articles found for your query.")
