'''config file'''

# DO NOT CHANGE ANY OF THESE SETTINGS
# Beam Base API URL
BEAM_URI = 'https://beam.pro/api/v1/'

# API Endpoints
OAUTH_URI = 'https://beam.pro/oauth/authorize?'
AUTHTOKEN_URI = 'oauth/token'
USERSCURRENT_URI = 'users/current'
CHATSCID_URI = 'chats/{cid}'
INTERACIVE_URI = "interactive/{channel}/robot"
INTERACTIVEHOSTS_URI = 'interactive/hosts'


# YOU CAN CHANGE THESE SETTINGS
# Redirect URL as stated in the OAUth Client under Website from
# https://beam.pro/lab and click AOUTH CLIENTS
REDIRECT_URI = 'https://auth.example.com'

# This is up to you to obtain, you may want to look at the 
# beam_oauth_example.py or you can find details about this  at
# https://dev.beam.pro/reference/oauth/index.html
ACCESS_TOKEN = 'REPLACE_WITH_YOUR_OAUTH_ACCESS_TOKEN'

# Provided when OAuth app is created, you can get this from
# https://beam.pro/lab and click AOUTH CLIENTS
CLIENT_ID = 'REPLACE_WITH_YOUR_CLIENT_ID'

# Permission for the chatbot a list of scopes can be found at
# https://dev.beam.pro/reference/oauth/index.html
SCOPE = ('channel:details:self channel:update:self chat:chat chat:connect '
         'chat:giveaway_start interactive:robot:self user:details:self')

# This is for interactive 2.0 and you can get this by going to
# https://beam.pro/i/studio go to the editor of your project and 
# going to the code tab at the top of the page
GAME_ID = '12345'

# Packet ID Number
PACKETID = 0
