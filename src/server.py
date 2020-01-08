# server.py - main app entrypoint
# @author jlacson

from flask import Flask, make_response
import playsound

# define our variables
# TODO: pull from env vars when we dockerize
DEBUG = True
PORT  = 9999

# define our flask app
flask_app = Flask(__name__)

# define endpoints here
@flask_app.route('/')
def home():
    # TODO: make a template we can serve up
    return make_response("Hello World!")

@flask_app.route('/heartbeat')
def heartbeat():
    return make_response(0)

# run our flask app here
if __name__ == "__main__":
    # bind to all interfaces, 
    # use debug and port vars set earlier
    flask_app.run(host='0.0.0.0', debug=DEBUG, port=PORT)
