from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    mobile: int
    email: str
    password: str
    confirm_password: str
    
