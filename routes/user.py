from typing import Union
from fastapi import FastAPI, Request , Form
from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import smtplib
from email.message import EmailMessage

# import pyotp
# import time
# import qrcode


user = APIRouter()
data=[]

templates = Jinja2Templates(directory="templates")
user.mount("/static", StaticFiles(directory="static",html=True),name="static")

@user.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@user.post("/submit")
def submit(name: str = Form(),emailAddress:str=Form(),message:str=Form()):
    print(name)
    print(emailAddress)
    print(message)
    
    email_address = "alexdenwise@gmail.com" #type mail address
    email_password = "ujqjkldmngpqnfrr"
    
    #create email
    msg = EmailMessage()
    msg['Subject'] = "Do.not.reply"
    msg['From'] = email_address
    msg['To'] = "vv7097@srmist.edu.in" #type mail id
    msg.set_content(
    f"""\
        Name : {name}
        Email: {emailAddress}
        Message: {message}
        """,
    )
    
   #send email
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email_address,email_password)
        smtp.send_message(msg) 
    
    return "Successfully sent"
   

@user.post("/write")
async def write_data(user: User):
    data.append(user.dict())
    return data

@user.get("/{id}")
async def read_data(id: int):
    return data[id]


@user.put("/user/{id}")
async def update_data(id: int ,user: User):
    data[id] = user
    return data


@user.delete("/delete/user/{id}")
async def delete_data(id : int):
    data.pop(id)
    return data

# key = pyotp.random_base32()

# # -------- Code for the time based one time password (TOTP) ---------
# totp = pyotp.TOTP(key)

# print(totp.now())
# input_code = input("Enter 2FA Code: ")

# print(totp.verify(input_code))
# if(totp.verify(input_code)==1):
#     print("Successfully verified")
# else:
#     print("No")
# time.sleep(30)
# print(totp.now())
