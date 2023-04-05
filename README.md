# Telegram Bots
This repository contains two Python scripts that demonstrate how to use the Telegram Bot API to send messages to a Telegram user or group.

## Motivator
motivator.py is a script that sends a motivational quote to a Telegram user or group at random intervals. The script uses the Quotable API to generate a random quote about education. You can set up a Telegram bot and use this script to send motivational messages to yourself or your friends!

To use the script, replace the BOT_TOKEN and CHAT_ID variables with your own Telegram bot token and chat ID. Then, run the script with the command python motivator.py.

## Time Left
timeLeft.py is a script that reminds a Telegram user or group about an upcoming event at a specific time every day. The script uses the World Time API to get the current time in Colombo, Sri Lanka, and sends a message at 3:30 AM every day reminding the user how many days are left until a specified date (in this case, October 8, 2023).

To use the script, replace the BOT_TOKEN and CHAT_ID variables with your own Telegram bot token and chat ID. Then, run the script with the command python timeLeft.py.

## Requirements
Both scripts require the requests and telegram modules to be installed. You can install these modules using pip with the command 
```
pip install -r requirements.txt.
```

File Structure
The file structure of this repository is as follows: <br>
├── motivator.py <br>
├── timeLeft.py <br>
├── requirements.txt <br>
└── README.md

* motivator.py - Script that sends a motivational quote to a Telegram user 
* timeLeft.py - Script that reminds a Telegram user, about upcoming event at a specific time every day.


## Credits

The scripts were created by [MrBhanuka](https://github.com/mrbhanukab).

[![website](https://img.shields.io/badge/Github%20Page-mrbhanukab.github.io-lightgrey?style=for-the-badge&logo=GitHubr&logoColor=white)](https://mrbhanukab.github.io/) <br>
[![github](https://img.shields.io/badge/Github-mrbhanukab-%23333?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/mrbhanukab) <br>
[![twitter](https://img.shields.io/badge/Twitter-mrbhanuka-%2300acee?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/mrbhanuka)