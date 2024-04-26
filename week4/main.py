from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from typing import Optional

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="secret")

# 創建靜態文件目錄
app.mount("/static", StaticFiles(directory="static"), name="static")

# 創建模板，指定模板的目錄位置為 "templates"
templates = Jinja2Templates(directory="templates")

# 定義 verification 功能
async def verify_user(username: str, password: str):
    return username == "test" and password == "test"

# Homepage
@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse(request=request, name="homepage.html")

# Verification Endpoint (sign in)
@app.post("/signin", response_class=HTMLResponse)
async def sign_in(request: Request, username: str = Form(None), password: str = Form(None), checkbox: Optional[bool] = Form(False)):
    if not username or not password:
        return RedirectResponse(url="/error?message=Please enter username and password", status_code=303)
    if await verify_user(username, password):
        # 設置用戶狀態為已登入
        request.session["SIGNED-IN"] = True
        return RedirectResponse(url="/member", status_code=303)
    else:
        return RedirectResponse(url="/error?message=Username or password is not correct", status_code=303)

# Verification Endpoint (sign out)
@app.get("/signout", response_class=HTMLResponse)
async def sign_out(request: Request):
    # 將 "SIGNED-IN" 狀態設置為 FALSE
    request.session["SIGNED-IN"] = False
    # 在登出時，清除用戶 session 中的相關資訊
    request.session.clear()
    # 重新導向到 homepage
    return RedirectResponse(url="/", status_code=303)

# Member page
@app.get("/member", response_class=HTMLResponse)
async def member_page(request: Request):
    if "SIGNED-IN" not in request.session or not request.session["SIGNED-IN"]:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse(request=request, name="successpage.html")

# Error page
@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request, message: Optional[str] = Query(None)):
    if message == "Please enter username and password":  
        return templates.TemplateResponse(request=request, message=message, name="errorpage1.html")
    if message == "Username or password is not correct":
        return templates.TemplateResponse(request=request, message=message, name="errorpage2.html")