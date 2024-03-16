from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class item(BaseModel):
    studentNumber : int


def split_number(n):
    n_str = str(n)[0:3]
    return int(n_str)

def Fixed_field(n):
   n_str = str(n)[3:9]
   return int(n_str)

def index(n):
    n_str = str(n)[9:11]
    return int(n_str)


@app.post("/Home")
def s_t(item : item):
    if len(str(item.studentNumber)) != 11:
        return "The number of digits entered is incorrect"
    if not 402 >= split_number(item.studentNumber, 8) >= 400 :
        return "The year field is incorrect"
    if Fixed_field(item.studentNumber) != 114150:
        return "The fixed field is wrong"
    if not 99 >= index(item.studentNumber) >= 1:
        return "The index part is wrong"
    return f"student number is correct : {item.studentNumber}"



