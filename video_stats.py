# Importing the requests library
import requests

# Importing OS library to read the .env variables
import os

# Importing the load_dotenv function to load variables from an .env file
from dotenv import load_dotenv

# Reads the .env file and add its values to the environment
load_dotenv(dotenv_path='./.env')

# Get the value of API_KEY from environment variables
API_KEY = os.getenv('API_KEY')


def get_playlist_id(CHANNEL_HANDLE: str) -> str:
    """
    Get the uploads playlist ID for a specific YouTube channel.

    Args:
        CHANNEL_HANDLE (str): YouTube channel's handle (name).

    Returns:    
        str: The uploads playlist ID.

    Raises:
        requests.exceptions.RequestException: If the HTTP request fails.
    """

    try:
        # URL for getting a channel's resource data
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'

        # GET-request
        response = requests.get(url)

        # Checks for HTTP errors
        response.raise_for_status()

        # Python dictionary with the recieved data about the YT channel
        data = response.json()

        # YT channel's uploads playlist ID extraction from the <data> dictionary
        channel_items = data["items"][0]
        uploads_playlist_id = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        print(f"\n=== Succeed to fetch the {CHANNEL_HANDLE} channel data. ===\n")

        # Returns the YT channel's uploads playlist ID
        return uploads_playlist_id
    
    # Excepting the HTTP-error if the .raise_for_status() method raises an HTTP-error
    # The RequestException class is a parent class for an HTTP-error  
    except requests.exceptions.RequestException:
        print(f"\n=== Failed to fetch the {CHANNEL_HANDLE} channel data. ===\n")
        raise
    

# Runs only when executed directly
# forHandle parameter (YT channel's name) in the parentheses
if __name__ == "__main__":
    get_playlist_id('MrBeast')
