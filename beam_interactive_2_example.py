'''
Connects to the Beam Interactive 2.0 and outputs
recieved data to the console
'''

import asyncio
from json import dumps, loads
from random import randint

import requests
import websocket

import config

# enables a detailed trace of what is happening when connecting
# though websockets, Change to False to switch it off
websocket.enableTrace(False)
# Creates the websocket Object
WS = websocket.WebSocket()
CONFIG = config

def _buildurl(path):
    return CONFIG.BEAM_URI + path

def get_endpoints():
    '''Gets the Interactive 2.0 server addresses'''
    data = dict(client_id=config.CLIENT_ID)
    # Creates the header for the request
    header = {'Media-Type': 'application/json',
              'Authorization': 'Bearer ' + CONFIG.ACCESS_TOKEN}
    # Get the request and return the responce
    url = _buildurl(CONFIG.INTERACTIVEHOSTS_URI)
    return requests.get(url=url, data=data, headers=header).json()

def _random_endpoint(endpoint):
    rnd = randint(0, len(endpoint) - 1)
    return endpoint[rnd]['address']

@asyncio.coroutine
def message(msg):
    '''Sends a message to the interactive 2.0 server.'''
    # send the packet to the data
    WS.send(dumps(msg))

@asyncio.coroutine
def connect_interactive():
    '''Connects to a randomly selected interactive 2.0 server and authenticates'''
    # gets a random server endpoint
    endpoint = _random_endpoint(get_endpoints())

    # print to console that connecting to a server
    print('Connecting to {} Interactive 2.0 server...'.format(endpoint))

    # Generates header for the connection to the endpoint (REQUIRED)
    header = ['Authorization: Bearer {}'.format(CONFIG.ACCESS_TOKEN),
              'X-Interactive-Version: {}'.format(CONFIG.GAME_ID),
              'X-Protocol-Version: 2.0']
    # connect to server
    WS.connect(endpoint, header=header)


@asyncio.coroutine
def recieve_interactive():
    '''listens for interactive events and prints to the console'''

    # create a Ready payload
    payload = {"type": "method",
               "id": 0,
               "method": "ready",
               "params": {"isReady": True},
               "discard": True}
    print('Sending Ready message to the connected server')
    # sends the Ready payload to the connected server
    yield from message(payload)

    # loop while connected
    while WS.connected:
        # This can be change to however you wich to handle
        # the interactive events
        print(loads(WS.recv()))
    # close connection when disconnecting
    WS.close()


if __name__ == '__main__':
    LOOP = asyncio.get_event_loop()

    try:
        LOOP.run_until_complete(connect_interactive())
        LOOP.run_until_complete(recieve_interactive())
    finally:
        LOOP.close()
