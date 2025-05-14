import requests

url = "https://CKone20.github.io/Instruments/Instruments.json"

try:
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()

    print("🎬 Movie Database:\n")

    for movie in data:
        print(f"🎞️  Name: {movie['name']}")
        print(f"📝 Description: {movie['description']}")
        print("📋 Specifications:")
        for key, value in movie["specifications"].items():
            print(f"   - {key.capitalize()}: {value}")
        print(f"🏷️ Tags: {', '.join(movie['tags'])}")
        print("-" * 40)

except requests.exceptions.RequestException as e:
    print("🔴 Failed to fetch data:", e)
except ValueError:
    print("🔴 Failed to decode JSON.")
except Exception as e:
    print("🔴 An unexpected error occurred:", e)
