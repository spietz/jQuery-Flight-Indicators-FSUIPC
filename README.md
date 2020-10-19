# The jQuery Flight Indicators Plugin linked to FSUIPC

The [Flight Indicators jQuery Plugin](https://github.com/sebmatton/jQuery-Flight-Indicators)
is linked to [FSUIPC](http://www.fsuipc.com/) to display flight simulator
(e.g. msfs2020) instruments from any device on the local network using
Flask.

## Usage
* Install the Python3 dependencies
```
pip install -r requirements.txt 
```
* Run FSUIPC.
* Run the flask server
```
python3 server.py
```
* From any device on the local network open the http://HOST:5000
  (where HOST is local ip address of machine running FSUIPC and the
  server)

## Credits
* https://github.com/sebmatton/jQuery-Flight-Indicators
* https://github.com/tjensen/fsuipc
* http://www.fsuipc.com/

## TODO
- [ ] do not use hardcoded update interval
- [ ] background texture
- [ ] full screen mode
