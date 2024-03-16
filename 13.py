from fastapi import FastAPI


app = FastAPI()


@app.post("/Home")
def marital_status(marital_statusn: str):
    if marital_statusn == "متاهل":
        return "He is married"
    if marital_statusn == "مجرد":
        return "He is single"
    else:
        return "is wrong value"
    