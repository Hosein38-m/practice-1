from fastapi import FastAPI

app = FastAPI()


def split_number(n):
    n_str = str(n)[0:3]
    return int(n_str)

def Fixed_field(n):
   n_str = str(n)[3:9]
   return int(n_str)

def index(n):
    n_str = str(n)[9:11]
    return int(n_str)


@app.get("/Home/{studentNumber}")
def s_t(studentNumber: int):
    if len(str(studentNumber)) != 11:
        return "The number of digits entered is incorrect"
    if not 402 >= split_number(studentNumber) >= 400 :
        return "The year field is incorrect"
    if Fixed_field(studentNumber) != 114150:
        return "The fixed field is wrong"
    if not 99 >= index(studentNumber) >= 1:
        return "The index part is wrong"
    return f"student number is correct : {studentNumber}"

