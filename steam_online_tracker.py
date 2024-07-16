import requests
import time
from datetime import datetime

def get_user_status(api_key, steam_id):
    url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}"
    try:
        response = requests.get(url)
        data = response.json()

        # Retrieve user information
        if 'response' in data and 'players' in data['response'] and len(data['response']['players']) > 0:
            player = data['response']['players'][0]
            return player['personastate']
        else:
            print("Error retrieving user data.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Input API key and Steam ID
    api_key = input("Enter your Steam API key: ").strip()
    steam_id = input("Enter the Steam ID of the user: ").strip()
    
    online_status = None

    while True:
        current_status = get_user_status(api_key, steam_id)

        # Check if the status has changed to "online"
        if current_status is not None and current_status == 1 and online_status != 1:
            online_status = current_status
            print(f"The user came online at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        time.sleep(60)  # Check the status every 60 seconds

if __name__ == "__main__":
    main()