from telethon.sync import TelegramClient

api_id = 'Your_Api_Id_here'
api_hash = 'Your_Api_hash_here'

group_username = 'mturkupdate'

# Initialize the Telegram client
with TelegramClient('session_name', api_id, api_hash) as client:
    group_entity = client.get_entity(group_username)
    
    # Get the participants in the group
    participants = client.get_participants(group_entity)
    
    # Iterate through the participants and print user IDs and account names
    for i, participant in enumerate(participants):
        user_id = participant.id
        account_name = participant.username
        profile_name = participant.first_name
        
        print(f"{i+1} User ID: {user_id}, Username : {account_name}, Profile Name: {profile_name}")
