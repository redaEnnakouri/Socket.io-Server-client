import socketio
import time

sio = socketio.Client()


@sio.on("connect")
def on_connect():
    print('connected to server')
    message="hi My Name is Ennakouri"
    print('Message : '+message)
    sio.emit('data',data=message)

@sio.on("disconnect")
def on_disconnect():
    print('disconnected from server')
    
@sio.on('response')
def on_response(data):
    print('Reponse : '+data)

sio.connect("http://localhost:6001")

try:
  # sio.wait() # doesn't raise it, so have to implement it manually ;-)
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  print("handling interrupt...")
  sio.disconnect()

print("done")
