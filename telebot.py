from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai
import sys

class Reference:
    '''
    A Class to store previously response from the ChatGPT API
    '''
    
    def __init__(self) -> None:
        self.response = ""


load_dotenv()
API_TOKEN = os.getenv("OpenAI_API_KEY")

reference = Reference()

TOKEN = os.getenv("Token")

#Model name 
Model_name  ="gpt-3.5-turbo"

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def clear_past():
    """
A Function to clear previous conversation and context.
    """
    reference.response = "" 

    @dp.message_handler(commands=['start', 'help'])  # Use 'commands' instead of 'command'
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or `/help` command
    """
    await message.reply("Hi\nI am Echo bot!\nPowered by AIOGRAM.")
