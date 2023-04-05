import requests
import telegram
import asyncio
import random

# Replace with your Telegram bot token and chat ID
BOT_TOKEN = '6286586256:AAHjU_-U6nO1yiO5Sm6gVVTaR_NU7mqhtLo'
CHAT_ID = '##Your Telegram ID'

async def generate_motivational_quote():
    """Generate a motivational quote about education using an external API."""
    response = requests.get("https://api.quotable.io/random")
    quote = response.json()["content"]
    author = response.json()["author"]
    message = f"<b>{quote}</b>\n\n- <i>{author}</i>"
    return message

async def send_message(message):
    """Send a message via Telegram."""
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="HTML")

async def main():
    while True:
        # Generate a motivational quote about education
        message = await generate_motivational_quote()
        
        # Send the message to the user
        await send_message(message)
        print("Message sent:", message)

        # Sleep for a random amount of time between 4 and 8 hours
        sleep_time = random.randint(4, 8) * 60 * 60
        print(f"Sleeping for {sleep_time/60/60} hours 😴")
        await asyncio.sleep(sleep_time)

if __name__ == '__main__':
    asyncio.run(main())
