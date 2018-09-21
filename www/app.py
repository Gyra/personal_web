#_*_
import logging
import asyncio
import os
import json
import time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)

def index(request):
    return web.Response(body=b'<h1>Initial</h1}')

@asyncio.coroutine
def init(loop):
    web_location = '127.0.0.1'
    web_port = 9000
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), web_location, web_port)
    logging.info('server started at http://' + web_location)
    return srv 

loop = asyncio.get_event_loop()
loop.run_untile_complete(init(loop))
loop.run_forever