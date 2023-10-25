from fastapi import FastAPI,WebSocket,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app=FastAPI()

@app.get("/")
async def home(request: Request):
	return templates.TemplateResponse("homepage.html",{"request":request})

websocket_list=[]
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
	await websocket.accept()
	if websocket not in websocket_list:
		websocket_list.append(websocket)
	while True:
		data = await websocket.receive_text()
		for web in websocket_list:
			if web!=websocket:
				await web.send_text(f"{data}")





