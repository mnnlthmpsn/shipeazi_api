from pydantic import BaseModel, EmailStr


class EmailSchema(BaseModel):
    email: EmailStr


class EmailBodySchema(BaseModel):
    recipient: EmailStr
    subject: str
    message: str
