# # import socketio

# # ''' Socketio server '''
# # sio_server = socketio.AsyncServer(
# #     # fast api is asgi applicatiopn. "Asynchronus server gateway interface"
# #     async_mode = 'asgi',
# #     cors_allowed_origins = []
# # )

# # ''' Socketio app '''
# # sio_app = socketio.ASGIApp(
# #     socketio_server= sio_server,
# #     socketio_path= 'sockets',
# #     static_files={
# #         '/':'./static/'
# #     }
# # )

# # ''' Adding an event to socketio server '''
# # @sio_server.event
# # async def connect(sid, environ, auth): #connect is the event that will be called from the client side
# #     print(f'{sid}: connected')


# # @sio_server.event
# # async def disconnect(sid):
# #     print(f'{sid}: disconnected')


# # @sio_server.event
# # async def message(data):
# #     print(f"from message", data)


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import socketio    
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()    
    
# sio = socketio.AsyncServer(async_mode='asgi')    
# socket_app = socketio.ASGIApp(sio, static_files={'/': 'static/'})    
# background_task_started = False    
    
    
# async def background_task():    
#     """Example of how to send server generated events to clients."""
#     count = 0
#     while True:
#         await sio.sleep(10)
#         count += 1
#         await sio.emit('my_response', {'data': 'Server generated event'})

# @sio.on('connect')
# async def on_connection(sid, _, m):
#     print(f'{sid}-Client connected')
#     await sio.emit('message', 'hello world!')
    
# @sio.on('disconnect')
# def test_disconnect(sid):
#     print(f'{sid}-Client disconnected')



# app.mount('/', socket_app)