from django.core.management.base import BaseCommand
from telegram.utils.request import Request
from django.conf import settings
from  telegram import Bot
from telegram.ext import Updater
import requests
from bot.views import *
from bot.admin_panel import  *

class Command(BaseCommand):
    help='Bu django telegram bot'

    def handle(self,*args,**options):
        request=Request(
        )
        bot=Bot(
            request=request,
            token=settings.TOKEN1,


        )

        print(bot.get_me())









updater = Updater(settings.TOKEN1)

updater.dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()