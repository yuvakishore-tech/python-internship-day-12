import requests
import json
from datetime import datetime

API_URL = "https://randomuser.me/api/"

def fetch_user_data():
    try:
        response = requests.get(API_URL, timeout=10)

        # Check HTTP status code
        if response.status_code != 200:
            print(f"❌ Failed to fetch data. Status code: {response.status_code}")
            return

        data = response.json()

        # Save raw JSON response to file
        filename = f"user_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        # Extract nested fields
        user = data["results"][0]
        name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
        email = user["email"]
        country = user["location"]["country"]
        age = user["dob"]["age"]

        # Display clean output
        print("✅ User Data Fetched Successfully\n")
        print(f"Name    : {name}")
        print(f"Email   : {email}")
        print(f"Country : {country}")
        print(f"Age     : {age}")
        print(f"\n📁 Raw API response saved to: {filename}")

    except requests.exceptions.Timeout:
        print("⏰ Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("🌐 Network error. Check your internet connection.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    fetch_user_data()
