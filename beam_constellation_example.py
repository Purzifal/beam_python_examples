'''An example of Beam Constellation'''

import asyncio
from json import dumps, loads
import websocket
import requests
import config

CONFIG = config
WS = websocket.WebSocket()


def _buildurl(path):
    return CONFIG.BEAM_URI + path

def get_user_data():
    ''' gets and returns the user information from beam '''
    # Create Data for request
    data = dict(client_id=CONFIG.CLIENT_ID)
    # Creates the header for the request
    header = {'Media-Type': 'application/json',
              'Authorization': 'Bearer ' + CONFIG.ACCESS_TOKEN}
    # Get the request and return the responce
    url = _buildurl(CONFIG.USERSCURRENT_URI)
    return requests.get(url=url, data=data, headers=header).json()


@asyncio.coroutine
def connect_constellation():
    '''connect to beam Constellation Server'''

    # Sets the header for the server connection
    header = ['authorization: Bearer {}'.format(CONFIG.ACCESS_TOKEN),
              'x-is-bot: True']
    
    # Connect to beam Constellation server with header
    WS.connect('wss://constellation.beam.pro/', header=header)

    # Setup the subscruption events that you would like info on
    sub = 'channel:{id}:hosted'.format(id=get_user_data()['channel']['id'])

    # construct the payload
    payload = {'type': 'method', 'method': 'livesubscribe',
               'params': {'events': [sub]}, 'id': 0}
    # Send the payload
    WS.send(dumps(payload))

@asyncio.coroutine
def run():
    '''listens for chat events and prints to the console'''

    # loop while connected
    while WS.connected:
        print(loads(WS.recv()))
    # close connection when not connected
    WS.close()


if __name__ == '__main__':
    LOOP = asyncio.get_event_loop()

    try:
        LOOP.run_until_complete(connect_constellation())
        LOOP.run_until_complete(run())
    finally:
        LOOP.close()
