import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = ""
with open("index.html", "r") as file:
    html = file.read()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    number = 1
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        message = data["message"]
        await websocket.send_json({
            "number": number,
            "message": message,
        })
        number += 1

if __name__ == "__main__":
    uvicorn.run("app:app")
