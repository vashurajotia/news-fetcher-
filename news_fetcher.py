import requests

query = input("What type of news are you interested in today? : ")
api = "86e5b73b9bfd4c7da3677ff20a50354c"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-13&sortBy=publishedAt&apiKey={api}"

r = requests.get(url)
print(r.json())

data = r.json()
articles = data["articles"]
for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n******************************************************************************************\n")
