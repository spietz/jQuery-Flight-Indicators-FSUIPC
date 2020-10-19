from flask import Flask, json
from flask_cors import CORS
from fsuipc import FSUIPC
import socket
from flask import render_template

# get hostname and ip ###
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

# setup flask app ###
app = Flask(__name__)
CORS(app)  # making cross-origin AJAX possible.

# setup fsuipc which communicates with the simulator ###
# see fsuipc documentation for offsets and types
fsuipc = FSUIPC()  # open link
fsuipc_setup = { # offset, type, transform
    'roll':(0x0000, "d", lambda x: int(-(x*(360./65536.)/65536.))),
    'pitch':(0x0578, "d", lambda x: int(-(x*(360./65536.)/65536.))),
    'heading':(0x0580, "d", lambda x: int(x*(360./65536.)/65536.)),
    'airspeed':(0x02BC, "d", lambda x: int(x/128.)),
    'altitude':(0x0574, "d", lambda x: int(x*3.28084)),
    'vertspeed':(0x02C8, "d", lambda x: int(x*60*3.28084/256.))
}
prepared = fsuipc.prepare_data([(v[0], v[1]) for k, v in fsuipc_setup.items()], True)  # prepare readings

# returns the fsuipc value subject to the transformations specified
@app.route('/values', methods=['GET'])
def get_values():

    fsuipc_values = prepared.read()  # read values from fsuipc

    values = {}  # add to dictonary and apply transform
    for i, (k, v) in enumerate(fsuipc_setup.items()):
        values[k] = v[2](fsuipc_values[i])

    return json.dumps(values)


# this provides a way to serve the index.html for the client device
@app.route('/')
def get_index():
    return render_template('index.html', host=host_ip)


if __name__ == '__main__':

    # display hostname and ip address
    print("Hostname :  ",host_name)
    print("IP : ",host_ip)

    # serve the api used in the javascript
    app.run(host= '0.0.0.0')  # visible on local network
    app.run()