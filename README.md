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
```
