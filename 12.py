from fastapi import FastAPI
import json

app = FastAPI()


def trust(n):
    with open("engineering_fields.json", "r", encoding="utf-8") as f :
        ob = json.load(f)
    for char in ob :
        if n in char:
            return True


@app.post("/Home")
def field(Field_of_Study:str):
    if trust(Field_of_Study) == True:
        return "field of study is True"
    else:
        return "wrong value"
    