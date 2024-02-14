from typing import Annotated
# from keycloak.realm import KeycloakRealm
from fastapi.responses import HTMLResponse, FileResponse
from fastapi import FastAPI, Depends

from backend.auth import get_user_info, oauth2_scheme, oauth2_scheme_psw
from backend.models import User

app = FastAPI()

#keycloakOpenid = KeycloakOpenID(
	#server_url='https://auth.ileska.fi',
	#client_id="pythonTest",
	# realm_name='PythonTest'
#)

@app.get("/")
async def root():
	return FileResponse("./frontend/index.html")

@app.get("/js/function.js")
async def functions():
	return FileResponse("./frontend/js/function.js")

@app.get("/css/style.css")
async def style():
	return FileResponse("./frontend/css/style.css")

@app.get("/keycloak.json")
async def keycloakJson():
	return FileResponse("./frontend/keycloak.json")

@app.get("/logout.html")
async def logout():
	return FileResponse("./frontend/logout.html")

@app.get("/secure")
async def secure(user: User = Depends(get_user_info)):
	return {"message": f"Hello {user.username} you have the following service: {user.realm_roles}"}

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme_psw)]):
    return {"token": token}
