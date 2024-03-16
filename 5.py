from fastapi import FastAPI
import json

app = FastAPI()

def is_center(n):
    with open("iran_provinces.json", "r", encoding="utf-8") as f:
        ob = json.load(f)
    for char in ob:
        if char in n:
            return True
        

@app.post("/home")
def provinces(province: str):
    if is_center(province) == True:
        return "correct"
    else:
        return "incorrect"