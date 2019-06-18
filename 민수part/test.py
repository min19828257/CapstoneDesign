from pyfirmata import Arduino, util
import requests
import json

board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()

while(1):
    board.analog[1].enable_reporting()
    result=board.analog[1].read()
    if(result<0.98):
        print("fire!!",result)
#        url="http://210.119.87.228:3000"
#        data={'msg':'Fire'}
#        headers={'Content-type':'application/json','Accept':'text/plain'}
#        r=requests.post(url,data=json.dumps(data),headers=headers)
    else:
        print("Nothing",result)

