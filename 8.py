from fastapi import FastAPI


app = FastAPI()


@app.post("/Home")
def Postal_code(code: int):
    if len(str(code)) == 10:
        return "number is valued"
    else:
        return "incorrect"