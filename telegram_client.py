import telepot  # Importing the telepot library
import config_util
from telepot.loop import MessageLoop  # Library function to communicate with telegram bot
from time import sleep  # Importing the time library to provide the delays in program

from formatter import Formatter
from google_client import GoogleClient
from zillow_client import ZillowClient


class TelegramClient:
    def __init__(self):
        self.bot = telepot.Bot(config_util.read_telegram_bot_token())
        print(self.bot.getMe())

    def start(self):
        MessageLoop(self.bot, self.handle).run_as_thread()
        print('Listening....')
        while 1:
            sleep(10)

    def handle(self, msg):
        # logger.info('handle: start', msg)
        chat_id = msg['chat']['id']  # Receiving the message from telegram
        url = msg['text']  # Getting text from the message
        new_dict = {'chat_id': chat_id, 'url': url}
        print(new_dict)
        self.process(new_dict)

    def process(self, request):
        processed_dict = self.get_home_details(request)
        address = self.get_address(processed_dict)
        new_dict = self.get_travel_distance(address)
        processed_dict.update(new_dict)
        if address:
            processed_dict['address'] = address
        print(processed_dict)
        formatter = Formatter()
        message = formatter.get_formatted_info(processed_dict)
        self.send_message(request['chat_id'], message)

    def send_message(self, chat_id, message):
        self.bot.sendMessage(chat_id, message)


    def get_home_details(self, request):
        processed_dict = {}
        if request and 'url' in request:
            zillow_client = ZillowClient()
            raw_dict = zillow_client.fetch(request['url'])
            processed_dict = zillow_client.process_fetched_content(raw_dict)
        return processed_dict

    def get_address(self, processed_dict):
        address = ""
        if processed_dict:
            address = f"{processed_dict['streetAddress']}, {processed_dict['city']}, {processed_dict['state']} {processed_dict['zipcode']} "
        return address

    def get_travel_distance(self, origin):
        google_client = GoogleClient()
        new_dict = google_client.get_travel_distance(origin)
        return new_dict


if __name__ == '__main__':
    telegram_client = TelegramClient()
    telegram_client.start()
