from telethon.sync import TelegramClient
from telethon import events
from telethon.errors import ChannelInvalidError
from affiliates import TeleGramAffiliate


class TelegramMessageForwarder:
    def __init__(self, api_id, api_hash, source_channel, destination_channel):
        self.api_id = api_id
        self.api_hash = api_hash
        self.source_channel = source_channel
        self.destination_channel = destination_channel
        self.client = TelegramClient('session', api_id, api_hash)
        self.telegram_affiliate = TeleGramAffiliate()

    async def forward_messages(self, event):
       
        message=event.message.message
        message,first_link, file_path = self.telegram_affiliate.modify_message(message, event)   
        event.message.message = message

        try:
            await self.client.send_message(self.destination_channel, message)
            print(f"Message forwarded: {message}")
        except Exception as e:
            print(f"Failed to forward message: {str(e)}")

    def start(self):
        print("Start")
        self.client.add_event_handler(self.forward_messages, events.NewMessage(chats=self.source_channel))
        self.client.start()
        self.client.run_until_disconnected()

# Usage example
api_id = 1958908
api_hash = '21d35d34c158be29142b85527b4128ab'
source_channel = 'testgmnw'
destination_channel = 'testgmnw'

forwarder = TelegramMessageForwarder(api_id, api_hash, source_channel, destination_channel)
forwarder.start()
