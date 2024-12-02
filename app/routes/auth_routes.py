from typing import Annotated
from fastapi import APIRouter, Form, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
import starlette.status as status
from fastapi.templating import Jinja2Templates

# import service functions
from app.services.auth_service import *

from app.models.user import User

router = APIRouter()

# set location for templates
templates = Jinja2Templates(directory="app/view_templates")


@router.get("/login", response_class=HTMLResponse)
async def getLogin(request: Request):


    # note passing of parameters to the page
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login")
async def postLogin(request: Request, response: Response,  userForm: Annotated[User, Form()]) :
    auth_user = userLogin(userForm)
    response = RedirectResponse(url="/product/", status_code=status.HTTP_302_FOUND)
    print(auth_user.session.refresh_token)
    response.set_cookie(
        key = "access_token",
        # value= f"Bearer {auth_user.session.access_token}",
        value= auth_user.session.access_token,
        httponly=True,
    )
    response.set_cookie(
        key = "refresh_token",
        value= auth_user.session.refresh_token,
        httponly=True,
    )
    return response


@router.get("/register", response_class=HTMLResponse)
async def getRegister(request: Request):


    # note passing of parameters to the page
    return templates.TemplateResponse("auth/register.html", {"request": request})

@router.post("/register")
async def postRegister(request: Request, userForm: Annotated[User, Form()]) :
    auth_user  = userRegister(userForm)
    #print(auth_user.session.access_token)
    return RedirectResponse(url="/product/", status_code=status.HTTP_302_FOUND)

@router.get("/logout", response_class=HTMLResponse)
async def getLogout(request: Request, response: Response) :
    
    # logout from Supabase (clear tokens)
    result = userLogout()

    # set redirect to /product
    response = RedirectResponse(url="/product/", status_code=status.HTTP_302_FOUND)

    # delete session cookies
    response.delete_cookie("access_token")
    response.delete_cookie("redresh_token")
    return response