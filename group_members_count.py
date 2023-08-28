from telethon.sync import TelegramClient

api_id = '26844307'
api_hash = '48fb030ae74cdc378e2871aa736b155b'

# group_username = 'mturkupdate'
# group_username = 'amazonmturkk'
# group_username = 'amazon_mturk'
group_username = 'mturkaccountschats'

# Initialize the Telegram client
with TelegramClient('session_name', api_id, api_hash) as client:
    group_entity = client.get_entity(group_username)
    participants_count = client.get_participants(group_entity).total

print(f"Total participants in the group: {participants_count}")