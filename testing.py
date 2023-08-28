import time
import json
from telethon.sync import TelegramClient

api_id = 'Your_Api_Id_here'
api_hash = 'Your_Api_hash_here'

group_username = 'mturkupdate'


# Initialize the Telegram client
with TelegramClient('session_name', api_id, api_hash) as client:
    group_entity = client.get_entity(group_username)
    
    # Always save the index value to the file, even if an error occurs
    try:
        # Read the last sent participant's index from the file
        with open('last_sent_index.txt', 'r') as file:
            last_sent_index = int(file.read().strip())
            print(last_sent_index)
    except FileNotFoundError:
        last_sent_index = 35
        print(last_sent_index)
    
    # Get the participants in the group
    participants = client.get_participants(group_entity)
    profile_name = participant.first_name

    # Start from the last sent index or the beginning
    start_index = last_sent_index

    # Define the batch size and sleep times
    batch_size = 10
    short_sleep_time = 5
    long_sleep_time = 3 * 60  # 5 minutes in seconds
    
    for i in range(start_index, len(participants), batch_size):
        batch = participants[i:i + batch_size]







    # Iterate through the participants and print user IDs and account names
    # for i, participant in enumerate(participants):
    #     user_id = participant.id
    #     account_name = participant.username
    #     profile_name = participant.first_name
        
    #     print(f"{i+1} User ID: {user_id}, Username : {account_name}, Profile Name: {profile_name}")



