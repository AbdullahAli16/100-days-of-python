# Day: 90 (Ex: 10 "News App")

import requests

country=input("Enter the 2-letter country-code (e.g us, in, pk etc): ").lower()
category=input("Enter category (📈 Business,🎮 Entertainment,🌍 General,🏥 Health,🧬 Science,⚽ Sports,💻 Technology): ").lower()

API_key="dcff6ba480224fafa6af77d6983d6334"
url=f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_key}"

response=requests.get(url)
data=response.json()

print("\n📰 Top Headlines:\n")
for count, article in enumerate(data["articles"],start=1):
    
    if count>4:
        break
    else:
        source= article["source"]["name"]
        author= article.get("author")   
        title= article["title"]
        description= article.get("description")
        article_link= article["url"]

        print(f"{count} - Source: {source}")
        print(f"Written by: {author}")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Read more: {article_link}\n")

print("-- End of Headlines --")