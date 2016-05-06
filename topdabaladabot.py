#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import time
import telepot

class TelegramBot(telepot.Bot):
    _answerer = None
    _bot_data = None

    def __init__(self, *args, **kwargs):
        super(TelegramBot, self).__init__(*args, **kwargs)
        self._answerer = telepot.helper.Answerer(self)
        self._bot_data = self.getMe()

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        #print('Chat Message:', content_type, chat_type, chat_id)

        if chat_type == "private" or msg['text'].lower().find(
                self._bot_data['username'].lower()) > -1:
            reply = "Faaala {}, seu arrombado!".format(msg['from']['first_name'])
            self.sendMessage(chat_id, reply)

    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        #print('Callback Query:', query_id, from_id, query_data)

    def on_inline_query(self, msg):
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        #print('Inline Query:', query_id, from_id, query_string)

        def compute_answer():
            # Compose your own answers
            articles = [{'type': 'article',
            		'id': 'abc', 'title': query_string, 'message_text': query_string}]

            return articles

        self._answerer.answer(msg, compute_answer)

    def on_chosen_inline_result(self, msg):
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
        #print('Chosen Inline Result:', result_id, from_id, query_string)


# Bot Instantiation and execution
TOKEN = "TOKEN-HERE"
topDaBalada = TelegramBot(TOKEN)
topDaBalada.message_loop()
print("listening...")

while True:
    time.sleep(5)

# outputMessage = botData['first_name'] + " na área."
# print(outputMessage);
