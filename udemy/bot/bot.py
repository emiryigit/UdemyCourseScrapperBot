# UdemyCourseScrapperBot - A Simple Udemy Free Courses Scrapper Bot (Updated)  

# Copyright (C) 2022-Present by Body Catcher <https://github.com/BodyCatcher>

import asyncio

from telethon import TelegramClient
from udemy import api_hash, api_id, token


class UdemyCourseScrapperBOT(TelegramClient):
    def __init__(self):
        super().__init__("udemycoursescrapperbot", api_id=api_id, api_hash=api_hash)

    async def __start(self):
        await super().start(bot_token=token)
        me = await self.get_me()
        print(f"<<<  UdemyCourseScrapperBot: Started at @{me.username}  >>>\n")
        await super().run_until_disconnected()

    def start_(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__start())
