#!/usr/bin/env python3

from os import getenv
from Aashii import Server
from Aashii.handlers import handlers

token = getenv("TOKEN")
database_url = getenv("DATABASE_URL")
interval = int(getenv("POLL_INTERVAL", 1))
listen = getenv("LISTEN")
port = int(getenv("PORT", 0))
url = getenv("URL")
server = Server(token, database_url, handlers)

if url:
    server.listen(listen, port, url, token)
else:
    server.poll(interval)
