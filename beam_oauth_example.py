'''
Interact with Beam API and get access token information
'''

from datetime import datetime, timedelta
import webbrowser
import requests
from requests_oauthlib import OAuth2Session
import config

CONFIG = config

def _buildurl(path):
    return CONFIG.BEAM_URI + path

def generate_authorizationcode():
    ''' Generates the authorization code '''

    # Sets up the OAuth URL to generate authorization code
    oauth = OAuth2Session(CONFIG.CLIENT_ID,
                          redirect_uri=CONFIG.REDIRECT_URI,
                          scope=CONFIG.SCOPE)
    # Forms an authorization URL
    authorization_url, state = oauth.authorization_url(CONFIG.OAUTH_URI)
    state = state
    # Opens a new tab in browser for permission agreement and
    # short code retrieval
    webbrowser.open_new(authorization_url)

def get_access_token():
    ''' Gets Access token from a authorization code entered by the user '''

     # Get the user to enter the authorization code
    code = input('Please enter your authorization code : ')

    # Creates the data used to send to the the beam API to access
    # the access and refresh token information
    data = dict(client_id=CONFIG.CLIENT_ID, code=code,
                redirect_uri=CONFIG.REDIRECT_URI,
                grant_type='authorization_code')

    # Generates the header for the request
    header = {'Media-Type': 'application/json'}

    # gets the the Access and Refresh tokens and returns them
    # to be processed
    responce = requests.post(url=_buildurl(CONFIG.AUTHTOKEN_URI), data=data, headers=header).json()
    return responce

def run():
    ''' get access token information and save to the data base '''
    # Generate authorization code
    generate_authorizationcode()

    # Get and store access token information
    data = get_access_token()

    # adds the 'expires_in' seconds to the current date and time
    expire_conversion = datetime.now() + timedelta(seconds=data['expires_in'])

    # updates the access token expiry to date and time format
    data['expires_in'] = expire_conversion.__str__()

    # prints the OAuth data to the console
    print(data)

run()
