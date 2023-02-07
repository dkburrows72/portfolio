import os
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

templates = Jinja2Templates(directory="templates")

router = APIRouter()

class Photo(BaseModel):
    filename: str
    description: str

photolist = []
filelist = os.listdir("static/album")
for f in filelist:
    photolist.append(Photo(filename=f, description=f"Insert desciption of {f} here"))

@router.get("/album", response_class=HTMLResponse)
async def album_home(request: Request):
    return templates.TemplateResponse("album.html", {"request": request, "photolist": photolist})

    
