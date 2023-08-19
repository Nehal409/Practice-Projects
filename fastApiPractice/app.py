# from fastapi import FastAPI
# from fastapi_socketio import SocketManager
# from fastapi.middleware.cors import CORSMiddleware
# import fastapi
# app = FastAPI()


# # Configure CORS settings
# origins = ["*"] 
# app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# sio = SocketManager(app=app, cors_allowed_origins=origins)

# @app.sio.on("connect")
# async def connect(sid, environ):
#     print(f"Client {sid} connected")
#     await sio.emit("message", {"message": "Connected!"}, to=sid)

# @sio.on('join')
# async def handle_join(sid, *args, **kwargs):
#     await sio.emit('lobby', 'User joined')

from fastapi import FastAPI
from fastapi_socketio import SocketManager
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"] 
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

sio = SocketManager(app=app)


@app.sio.on('join')
async def handle_join(sid, *args, **kwargs):
    await sio.emit('lobby', 'User joined')


@sio.on('test')
async def test(sid, *args, **kwargs):
    await sio.emit('hey', 'joe')