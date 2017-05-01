'''
Gets data from Beam Interactive and outputs to console

Based on old version of beam interactive example and updated
'''

import asyncio
from math import isnan
import requests
from beam_interactive import start, proto
import config

CONFIG = config

def _buildurl(path):
    return CONFIG.BEAM_URI + path

def userdata():
    ''' gets and returns the user information from beam '''
    # Create Data for request
    data = dict(client_id=CONFIG.CLIENT_ID)
    # Creates the header for the request
    header = {'Media-Type': 'application/json',
              'Authorization': 'Bearer ' + CONFIG.ACCESS_TOKEN}
    # Get the request and return the responce
    url = _buildurl(CONFIG.USERSCURRENT_URI)
    return requests.get(url=url, data=data, headers=header).json()


def join_interactive(channel):
    '''Retrieve interactive connection information.'''
    # Create Data for request
    data = dict(client_id=CONFIG.CLIENT_ID)
    # Creates the header for the request
    header = {'Media-Type': 'application/json',
              'Authorization': 'Bearer ' + CONFIG.ACCESS_TOKEN}
    # Get the request and return the responce
    url = _buildurl(CONFIG.INTERACIVE_URI).format(channel=channel)
    return requests.get(url=url, data=data, headers=header).json()


def on_error(error):
    '''Handle error packets.'''
    print('Oh no, there was an error!', error.message)


def on_report(report):
    '''Handle report packets.'''

    # Tactile Mouse Click Control
    for tactile in report.tactile:
        if tactile.pressFrequency:
            print('Tactile report received!', tactile, sep='\n')

    # Joystick Mouse Movement Control
    for joystick in report.joystick:
        if not isnan(joystick.coordMean.x) and not isnan(joystick.coordMean.y):
            print('Joystick report received!', joystick, sep='\n')



@asyncio.coroutine
def run():
    '''Run the interactive app.'''

    # Get the channel ID
    channel_id = userdata()['channel']['id']

    # Get Interactive connection information.
    data = join_interactive(channel_id)

    # Initialize a connection with Interactive.
    connection = yield from start(data['address'], channel_id, data['key'])

    # Handlers, to be called when Interactive packets are received.
    handlers = {
        proto.id.error: on_error,
        proto.id.report: on_report
    }

    # wait_message is a coroutine that will return True when it receives
    # a complete packet from Interactive, or False if we got disconnected.
    while (yield from connection.wait_message()):

        # Decode the Interactive packet.
        decoded, _ = connection.get_packet()
        packet_id = proto.id.get_packet_id(decoded)

        # Handle the packet with the proper handler, if its type is known.
        if packet_id in handlers:
            handlers[packet_id](decoded)
        elif decoded is None:
            print('Unknown bytes were received. Uh oh!', packet_id)
        else:
            print('We got packet {} but didn\'t handle it!'.format(packet_id))

    connection.close()


if __name__ == '__main__':
    LOOP = asyncio.get_event_loop()

    try:
        LOOP.run_until_complete(run())
    finally:
        LOOP.close()
