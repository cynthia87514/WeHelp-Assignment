import mysql.connector
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="secret")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

con = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="********",
    database="website"
) 

async def verify_user(username2: str, password2: str):
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM `member` WHERE username = %s AND password = %s", (username2, password2))
    result = cursor.fetchone()
    return result[0] > 0

# Homepage
@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

# Verification Endpoint (sign up)
@app.post("/signup", response_class=HTMLResponse)
async def sign_up(request: Request, name: str = Form(None), username: str = Form(None), password: str = Form(None)):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM `member` WHERE username = %s", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        return RedirectResponse(url="/error?message=帳號已經被註冊", status_code=303)

    cursor.execute("INSERT INTO `member` (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
    con.commit()
    return RedirectResponse(url="/", status_code=303)

# Verification Endpoint (sign in)
@app.post("/signin", response_class=HTMLResponse)
async def sign_in(request: Request, username2: str = Form(None), password2: str = Form(None)):
    if await verify_user(username2, password2):
        request.session["SIGNED-IN"] = True
        # 從資料庫中取得會員名稱
        cursor = con.cursor()
        cursor.execute("SELECT id, name FROM `member` WHERE username = %s AND password = %s", (username2, password2))
        member_data = cursor.fetchone()
        if member_data:
            member_id = member_data[0]
            member_name = member_data[1]
            # 將會員 id, 名稱儲存在 session 中
            request.session.update({"member_id": member_id, "member_name": member_name})
        return RedirectResponse(url="/member", status_code=303)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼輸入錯誤", status_code=303)

# Verification Endpoint (create message)
@app.post("/createMessage", response_class=HTMLResponse)
async def create_message(request: Request, message: str = Form(None)):
    member_id = request.session["member_id"]
    cursor = con.cursor()
    cursor.execute("INSERT INTO `message` (member_id, content) VALUES (%s, %s)", (member_id, message))
    con.commit()
    return RedirectResponse(url="/member", status_code=303)

# Verification Endpoint (delete message)
@app.post("/deleteMessage", response_class=HTMLResponse)
async def delete_message(request: Request, message_id: int = Form(...)):
    member_id = request.session["member_id"]
    cursor = con.cursor()
    cursor.execute("DELETE FROM `message` WHERE id = %s AND member_id = %s", (message_id, member_id))
    con.commit()
    return RedirectResponse(url="/member", status_code=303)

# Verification Endpoint (sign out)
@app.get("/signout", response_class=HTMLResponse)
async def sign_out(request: Request):
    request.session["SIGNED-IN"] = False
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)

# Member page
@app.get("/member", response_class=HTMLResponse)
async def member_page(request: Request):
    if "SIGNED-IN" not in request.session or not request.session["SIGNED-IN"]:
        return RedirectResponse(url="/", status_code=303)
    member_name = request.session["member_name"]
    member_id = request.session["member_id"]
    cursor = con.cursor()
    cursor.execute("SELECT `member`.name, `message`.content, `message`.id, `message`.member_id FROM `message` JOIN `member` ON `message`.member_id = `member`.id ORDER BY `message`.time DESC")
    messages = cursor.fetchall()
    return templates.TemplateResponse("memberpage.html", {"request": request, "member_name": member_name, "messages": messages, "member_id": member_id})

# Error page
@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request, message: str): 
    return templates.TemplateResponse("errorpage.html", {"request": request, "message": message})


def shutdown_event():
    con.close()
app.add_event_handler("shutdown", shutdown_event)