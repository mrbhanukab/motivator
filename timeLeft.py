import datetime
import telegram
import asyncio
import requests

# Replace with your bot token and chat ID
BOT_TOKEN = '6286586256:AAHjU_-U6nO1yiO5Sm6gVVTaR_NU7mqhtLo'
CHAT_ID = '##Your Telegram ID'

async def get_current_time():
    """Get the current time in Colombo, Sri Lanka."""
    response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Colombo')
    response.raise_for_status()
    data = response.json()
    return datetime.datetime.fromisoformat(data['datetime'])

async def days_until_october_8_2023():
    """Calculate the number of days until October 8, 2023."""
    today = (await get_current_time()).date()
    target_date = datetime.date(2023, 10, 8)
    delta = target_date - today
    return delta.days

async def send_message(message):
    """Send a message via Telegram."""
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="HTML")

async def main():
    while True:
        now = (await get_current_time()).time()
        if now.hour == 3 and now.minute == 30:
            days = await days_until_october_8_2023()
            message = f"👋 Hey, just dropping in to remind you:\n\n⏳ <b><u>Only {days} days left</u></b> until your A-Level exam!\n\n🎉 You've got this! Keep going and stay focused!💪 You've come this far, so keep pushing and believe in yourself!\n\nAnd <b>Do the hard work especially when you don't feel like it</b> 💪😊"
            await send_message(message)
            print("msg sent")
            # Sleep for 24 hours
            print("Sleeping for 24 hours 😴")
            await asyncio.sleep(23 * 59 * 60)
            
        else:
            # Sleep for 1 minute
            print("Sleeping for 1 minute 😴")
            await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
