import requests
import time
from datetime import datetime

def get_user_info(api_key, steam_id):
    url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}"
    try:
        response = requests.get(url)
        data = response.json()

        # Retrieve user information
        if 'response' in data and 'players' in data['response'] and len(data['response']['players']) > 0:
            player = data['response']['players'][0]
            return {
                'personastate': player.get('personastate'),
                'personaname': player.get('personaname'),
                'profileurl': player.get('profileurl'),
                'avatar': player.get('avatar'),
                'lastlogoff': player.get('lastlogoff'),
                'timecreated': player.get('timecreated')
            }
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
        user_info = get_user_info(api_key, steam_id)

        if user_info:
            current_status = user_info['personastate']
            personaname = user_info['personaname']
            profileurl = user_info['profileurl']
            avatar = user_info['avatar']
            lastlogoff = user_info['lastlogoff']
            timecreated = user_info['timecreated']

            # Convert timestamps to human-readable format
            lastlogoff_str = datetime.fromtimestamp(lastlogoff).strftime('%Y-%m-%d %H:%M:%S') if lastlogoff else 'N/A'
            timecreated_str = datetime.fromtimestamp(timecreated).strftime('%Y-%m-%d %H:%M:%S') if timecreated else 'N/A'

            # Print user information
            print(f"User: {personaname}")
            print(f"Profile URL: {profileurl}")
            print(f"Avatar URL: {avatar}")
            print(f"Last Logoff: {lastlogoff_str}")
            print(f"Account Created: {timecreated_str}")
            
            # Check if the status has changed to "online"
            if current_status == 1 and online_status != 1:
                online_status = current_status
                print(f"The user came online at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        time.sleep(60)  # Check the status every 60 seconds

if __name__ == "__main__":
    main()