import jdatetime
from fastapi import FastAPI


def check_shamsi(d_str):
    obj_date = jdatetime.datetime
    try:
        obj_date.strptime(d_str, '%Y/%m/%d')
        return True
    except ValueError:
        return False

app = FastAPI()


@app.post("/home")
def date(date: str):
    if check_shamsi(date) == True:
        return "This date is correct"
    else:
        return "This date is incorrect"
