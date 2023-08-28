# Telegram Group Automation Script 📲

This repository contains a set of Python scripts that leverage the Telethon library to automate tasks within a Telegram group. The provided scripts offer various functionalities:

1. **Count Group Participants**

   `group_members_count.py` allows you to count the total number of participants in a specified Telegram group. It connects to the Telegram API and retrieves the participant count.

2. **List Group Participants**

   `group_members_list.py` enables you to list the participants of a Telegram group. It retrieves user IDs, account names, and profile names of participants and presents them in an organized manner.

3. **Send Customized Messages with Images**

   `message_group_members.py` automates sending customized messages with images to participants in a Telegram group. You can define the message text, attach images, and manage sending batches of messages.

## How to Use

### 1. API Creation

Before using any of the scripts, you need to create an API on Telegram's website:
1. Visit the [Telegram API website](https://my.telegram.org/auth?to=apps){:target="_blank"}.
2. Sign in with your Telegram account.
3. Create a new application to get your `api_id` and `api_hash`.

### 2. Installation

To run the scripts, you need to install the required libraries. Run the following command:

```bash
pip install telethon

# Usage

## Count Group Participants

To count the participants in a specific Telegram group, follow these steps:
1. Open `count_participants.py`.
2. Replace `'Your_Api_Id_here'` and `'Your_Api_hash_here'` with your actual API credentials.
3. Provide the `group_username` of the group you want to count participants for.

## List Group Participants

To list the participants of a Telegram group, do the following:
1. Open `list_participants.py`.
2. Insert your API credentials (`'Your_Api_Id_here'` and `'Your_Api_hash_here'`).
3. Specify the `group_username` of the group you want to list participants for.

## Send Customized Messages with Images

To send customized messages along with images to participants, proceed as follows:
1. Open `send_custom_messages.py`.
2. Replace `'Your_Api_Id_here'` and `'Your_Api_hash_here'` with your API credentials.
3. Customize the `group_username`, `image_path1`, `image_path2`, and `message_text` as needed.
4. The script will handle batch sending and sleep times automatically.
5. **Important:** Before running `send_custom_messages.py`, create a file named `last_sent_index.txt` and add an initial value (e.g., 45) to it.

# Libraries Used

- **telethon**: Python wrapper for the Telegram API, facilitating easy interaction with Telegram.
- **time**: Standard Python library for time-related functions.

# Notes

- Customize the provided scripts according to your specific requirements.
- Properly handle exceptions and errors to ensure robust usage.
- Always adhere to Telegram's terms of use and API guidelines.
