from fastapi import FastAPI
import json


app = FastAPI()


def is_cities(n):
    with open("province.json", "r", encoding="utf-8") as f:
        ob = json.load(f)

    for char in ob:
        if char in n:
            return True
        

@app.post("/Home")
def cities(city: str):
    if is_cities(city) == True:
        return "is correct"
    else:
        return "is incorrect"
    