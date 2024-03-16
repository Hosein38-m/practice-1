from fastapi import FastAPI


app = FastAPI()


@app.post("/Home")
def address(address: str):
    if 100 < len(address):
        return "correct"
    else:
        return "incorrect"

