# # Exercise 10... Question...News App in Python... 




# USe the newssAPI and the requests module to fetch the daily news related to different topics.

# Go to: https://newsapi.org/ and exlore the various options to build you application...








import requests

# Replace with your actual NewsAPI key from https://newsapi.org/
API_KEY = "YOUR_API_KEY_HERE"


def fetch_news(url, params):
    """Sends a GET request to NewsAPI and displays formatted articles."""
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raises an error for bad status codes (4xx or 5xx)
        data = response.json()

        if data.get("status") != "ok":
            print(f"\nAPI Error: {data.get('message', 'Unknown error')}")
            return

        articles = data.get("articles", [])
        if not articles:
            print("\nNo articles found for your query.")
            return

        print(f"\n--- Showing Top {min(len(articles), 10)} News Articles ---\n")
        for idx, article in enumerate(articles[:10], start=1):
            title = article.get("title") or "No Title"
            source = article.get("source", {}).get("name") or "Unknown Source"
            description = article.get("description") or "No description available."
            article_url = article.get("url") or ""

            print(f"{idx}. {title}")
            print(f"   Source: {source}")
            print(f"   Summary: {description}")
            print(f"   Read more: {article_url}")
            print("-" * 70)

    except requests.exceptions.RequestException as e:
        print(f"\nNetwork or HTTP Error occurred: {e}")


def main():
    categories = [
        "business",
        "entertainment",
        "general",
        "health",
        "science",
        "sports",
        "technology",
    ]

    while True:
        print("\n=== PYTHON DAILY NEWS APP ===")
        print("1. Top Headlines by Category")
        print("2. Search News by Topic / Keyword")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == "1":
            print("\nAvailable Categories:", ", ".join(categories))
            category = input("Enter a category: ").strip().lower()

            if category not in categories:
                print("Invalid category. Defaulting to 'general'.")
                category = "general"

            country = (
                input("Enter 2-letter country code (e.g., us, in, gb) [default: us]: ")
                .strip()
                .lower()
                or "us"
            )

            url = "https://newsapi.org/v2/top-headlines"
            params = {
                "apiKey": API_KEY,
                "category": category,
                "country": country,
                "pageSize": 10,
            }
            fetch_news(url, params)

        elif choice == "2":
            query = input("\nEnter a topic to search (e.g., Python, AI, SpaceX): ").strip()
            if not query:
                print("Search query cannot be empty.")
                continue

            url = "https://newsapi.org/v2/everything"
            params = {
                "apiKey": API_KEY,
                "q": query,
                "language": "en",
                "sortBy": "publishedAt",  # Options: relevancy, popularity, publishedAt
                "pageSize": 10,
            }
            fetch_news(url, params)

        elif choice == "3":
            print("Exiting News App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()