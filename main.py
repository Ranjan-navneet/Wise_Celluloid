from fastapi import FastAPI, Request ,Form
from routes.index import user
# import pyotp
# import time
# import qrcode
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static",html=True),name="static")

app.include_router(user)

# key = pyotp.random_base32()

# -------- Code for the time based one time password (TOTP) ---------
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

# -------- Code for the Hashed based message authenctication Code (HOTP) ---------
# Counter =0
# hotp = pyotp.HOTP(key)
# print(hotp.at(0))

# Hashed_OTP = hotp.verify(input("Enter Code: "),Counter)
# for Counter in range(1):
    # if(Hashed_OTP==True):
        # print("Successful")
    # else:
        # print("Try Again")
        # Counter+=1 

#---------- QR CODE Based Authentication --------------

# uri = pyotp.totp.TOTP(key).provisioning_uri(name="Cristiano", issuer_name="Wise Celluloid")

# print(uri)

# qrcode.make(uri).save("name.png")

# totp = pyotp.TOTP(key)
# QR_CODE = totp.verify(input("Enter Code: "))

# if(QR_CODE == True):
#     print("Successfully scanned")
# else:
#     print("Error!") 
    

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
