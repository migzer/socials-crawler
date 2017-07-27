# -*- coding: utf-8 -*-

from fbchat import Client
from fbchat.models import *

username = "miguel1601@hotmail.fr"
password = "Caligada35"
client = Client(username, password)

if not client.isLoggedIn():
    client.login(username, password)

client.sendMessage("test", thread_id="Yokaze", thread_type=ThreadType.USER)

client.logout()
