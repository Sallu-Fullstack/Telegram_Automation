from telethon.sync import TelegramClient

api_id = 'Your_Api_Id_here'
api_hash = 'Your_Api_hash_here'

# group_username = 'mturkupdate'
# group_username = 'amazonmturkk'
# group_username = 'amazon_mturk'
group_username = 'mturkaccountschats'

# Initialize the Telegram client
with TelegramClient('session_name', api_id, api_hash) as client:
    group_entity = client.get_entity(group_username)
    participants_count = client.get_participants(group_entity).total

print(f"Total participants in the group: {participants_count}")
