# beam_python_examples
Examples on how to do stuff with Beam in python

# Config
you will need edit the config.py with your own information
* OAuth access token 
* Client ID

# Examples
There are examples that cover certain aspects of the services offered by beam.pro. These are:-

* **OAuth** - getting access token data
* **Chat** - connect to chat and send a message
* **Interactive 1** - connect to the channel interactive and recieve packet data (Soon to be depreciated)
* **Interactive 2.0** - Connect to channel interactive 2 and recieve event data
* **Constellation** - Connect to Beam's Constellation server and subscribe to liveloading events

NOTE: All these examples are very basic for their functions and is not ment to be the all in 1 solution.

# Requirements

**Python:** 3.4  
**Libraries:** websocket-client, requests_oauthlib
  * **Windows:** pip install setup.py
  * **Raspberry Pi:** sudo pip3 install setup.py
  
# Run
* **Windows:** python *filename*.py
* **Raspberry Pi:** python3 *filename*.py
