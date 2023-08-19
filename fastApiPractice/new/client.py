import socketio
# import asyncio

sio_client = socketio.Client()

@sio_client.on('join')
def on_join(data):
    print('I\'m connected')

@sio_client.event
async def connect():
    print ('I\'m connected')

@sio_client.event
def disconnect():
    print ('I\'m disconnected')

def main():
    sio_client.connect(url='http://localhost:9999', 
                       wait_timeout = 3)
    sio_client.wait()

main()