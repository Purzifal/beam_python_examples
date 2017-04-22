'''config file'''

# Beam Base URL
BEAM_URI = 'https://beam.pro/api/v1/'

# API Endpoints
OAUTH_URI = 'https://beam.pro/oauth/authorize?'
AUTHTOKEN_URI = 'oauth/token'
USERSCURRENT_URI = 'users/current'
CHATSCID_URI = 'chats/{cid}'
INTERACIVE_URI = "interactive/{channel}/robot"

# Redirect URL as stated in the OAUth Client under Website

REDIRECT_URI = 'https://auth.example.com'

# This is up to you to obtain
ACCESS_TOKEN = 'REPLACE_WITH_YOUR_OAUTH_ACCESS_TOKEN'

# Provided when OAuth app is created
CLIENT_ID = 'REPLACE_WITH_YOUR_CLIENT_ID'

# Permission for the chatbot
SCOPE = ('channel:details:self channel:update:self chat:chat chat:connect '
         'chat:giveaway_start interactive:robot:self user:details:self')

# Packet ID Number
PACKETID = 0
