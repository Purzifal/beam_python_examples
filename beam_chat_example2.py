'''
A very basic chat bot using asyncio

If running on windows, run the command, chcp 65001
'''

import asyncio
from json import dumps, loads
from random import randint
import requests
import websocket
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

def get_chat_connections(cid):
    '''Gets the chat server information'''
    # Create Data for request
    data = dict(client_id=CONFIG.CLIENT_ID)
    # Creates the header for the request
    header = {'Media-Type': 'application/json',
              'Authorization': 'Bearer ' + CONFIG.ACCESS_TOKEN}
    # Get the request and return the responce
    url = _buildurl(CONFIG.CHATSCID_URI.format(cid=cid))
    return requests.get(url=url, data=data, headers=header).json()

def random_chat_endpoint(endpoints):
    '''rerurns a random chat server to connect to'''
    rnd = randint(0, len(endpoints) - 1)
    return endpoints[rnd]

def message(msg, method):
    '''Sends a chat message.'''
    # if msg is not a list then make it a list
    if not isinstance(msg, list):
        msg = [msg]

    # set up packet to send
    packet = {'type': 'method',
              'arguments': msg,
              'method': method,
              'id': CONFIG.PACKETID}

    # increment the PACKETID by 1
    CONFIG.PACKETID += 1

    # send the packet to the data
    WS.send(dumps(packet))

@asyncio.coroutine
def connect_chat():
    '''Connects to a randomly selected chat server and authenticates'''
    # Connect to random selected chat server

    #get user data and connection information
    udata = get_user_data()
    chatinfo = get_chat_connections(udata['channel']['id'])
    endpoint = random_chat_endpoint(chatinfo['endpoints'])

    # print to console that connecting to a server
    print('connecting to {} ...'.format(endpoint))

    # connect to server
    WS.connect(endpoint)

    # create auth payload
    payload = [udata['channel']['id'],
               udata['channel']['userId'],
               chatinfo['authkey']]

    # send auth payload to the connected server
    message(payload, 'auth')

@asyncio.coroutine
def run():
    '''listens for chat events and prints to the console'''
    # adds a delay to allow authentocation to process
    yield from asyncio.sleep(1)
    # sends a message to chat to say that the bot is connected
    message('bot connected to chat', 'msg')

    # loop while connected
    while WS.connected:
        print(loads(WS.recv()))
    # close connection when not connected
    WS.close()


if __name__ == '__main__':
    LOOP = asyncio.get_event_loop()

    try:
        LOOP.run_until_complete(connect_chat())
        LOOP.run_until_complete(run())
    finally:
        LOOP.close()
