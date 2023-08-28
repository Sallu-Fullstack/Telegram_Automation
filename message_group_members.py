import time
from telethon.sync import TelegramClient

api_id = '25792473'
api_hash = '93933d996baedd3feb3de57e7be39a85'

group_username = 'mturkupdate'

# Paths to the images you want to send
# image_path1 = r"D:\Mturk\Mturk_Ads_Salman.png"
image_path1 = r"D:\Mturk\Mturk_Ads_Waseem.jpeg"
image_path2 = r"C:\Users\HP\Downloads\mturkscreen3.png"
image_path3 = r"C:\Users\HP\Downloads\NOVA_TURK.jpeg"

# Customize your message
message_text = '''
Mturk Developers:
ID for Sales and Rental Available

Work Actively(Only Florida & Texas Ids)
Very Strong RDP And Proxy Secured Ids.
Need Experienced Worker....

Office Setup Bulk ID Available
On Best Cheap Price and Rental's also Available.

Us id available for rent : 
Rupees for Dollars Monthly

Above 50$ - 30 Rupees/$
Above 100$- 40 Rupees/$

Join out Telegram Group for more offers
👉 https://t.me/+9Z8ITxxLjhFmZmQ1
'''

# Initialize the Telegram client
with TelegramClient('session_name', api_id, api_hash) as client:
    group_entity = client.get_entity(group_username)
    
    # Always save the index value to the file, even if an error occurs
    try:
        with open('last_sent_index.txt', 'r') as file:
            last_sent_index = int(file.read().strip())
    except FileNotFoundError:
        last_sent_index = 45
    
    # Get the participants in the group
    participants = client.get_participants(group_entity)
    
    # Define the batch size and sleep times
    batch_size = 10
    short_sleep_time = 5
    long_sleep_time = 3 * 60  # 5 minutes in seconds
    
    
    # Iterate through the participants and send messages and images
    for i, participant in enumerate(participants[last_sent_index:], start=last_sent_index):
        try:
            # Send messages and images to the participant
            media_group = []
            with open(image_path1, 'rb') as image_file1:
                media_group.append(client.upload_file(image_file1))
            with open(image_path2, 'rb') as image_file2:
                media_group.append(client.upload_file(image_file2))
            with open(image_path3, 'rb') as image_file3:
                media_group.append(client.upload_file(image_file3))
            
            client.send_message(participant.id, message_text, file=media_group)
            
            print(f"{i+1}. Message and images sent to {participant.first_name}")
            
            # Add a short sleep time
            time.sleep(short_sleep_time)
            
            # Update the index and save it to the file
            last_sent_index = i
            with open('last_sent_index.txt', 'w') as file:
                file.write(str(last_sent_index))
            
            # If a batch is sent, take a long sleep
            if (i + 1) % batch_size == 0:
                print(f"Waiting for {long_sleep_time} seconds before sending the next batch...")
                time.sleep(long_sleep_time)
        
        except Exception as e:
            print(f"Failed to send to {participant.first_name}: {e}")
            # You can choose to continue with the next participant or break the loop
    
    print("Message sending process completed.")