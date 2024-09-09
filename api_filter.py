"""
Exercise:

Scenario:

You’re tasked with getting the latest news headlines from the News
API (a hypothetical public API for this exercise).
Your goal is to fetch the latest news articles, filter them based on specific
criteria, and return the results in a concise format.

Requirements:

    1.Fetch the latest news articles from a public API.
        •API Endpoint: https://jsonplaceholder.typicode.com/posts
        •Each article contains an id, title, and body.

    2.Filter the articles to include only those that contain the
    word “voluptatem” in their body.

    3.Return a list of dictionaries with only the id and title of the filtered
    articles.

Example:
    [
        {
            "id": 1,
            "title": "Title 1"
        },
        {
            "id": 3,
            "title": "Title 3"
        }
    ]

Bonus:
  •Sort the filtered articles alphabetically by their title.
  •Handle any potential errors, such as network issues or missing data.
"""

import requests

url = "http://jsonplaceholder.typicode.com/posts"


def fetch_and_filter_articles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        resp = response.json()
        articles = []
        for item in resp:
            if "voluptatem" in item["body"]:
                obj = {"id": item["id"], "title": item["title"]}
                articles.append(obj)
        articles.sort(key=lambda x: x["title"])
        return articles
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
