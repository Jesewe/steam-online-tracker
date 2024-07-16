# Steam Online Tracker

Steam Online Tracker is a Python script that monitors the online status of a specific Steam user. The script periodically checks the user's status and logs the time when the user comes online.

## Requirements

- Python 3.x
- `requests` library

## Getting Started

1. Clone the repository or download the script file.

2. Install the required library:
    ```sh
    pip install requests
    ```

3. Obtain your Steam API key from the [Steam API page](https://steamcommunity.com/dev/apikey).

4. Run the script:
    ```sh
    python steam_online_tracker.py
    ```

5. Enter your Steam API key and the Steam ID of the user you want to track when prompted.

## How It Works

The script sends periodic requests to the Steam Web API to check the online status of the specified user. If the user's status changes to "online", the script logs the current date and time.

## Example Usage

1. Run the script:
    ```sh
    python steam_online_tracker.py
    ```

2. Enter your API key and the Steam ID:
    ```sh
    Enter your Steam API key: YOUR_API_KEY
    Enter the Steam ID of the user: 76561198000000000
    ```

3. The script will output the time when the user comes online:
    ```sh
    The user came online at 2024-07-16 14:32:00
    ```

## Contributing
Contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
