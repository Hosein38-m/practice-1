from fastapi import FastAPI


app = FastAPI()


def number_standard_landline(n):
    return n[0:3]


@app.post("/Home")
def landline_number(number):
    if len(number) != 11:
        return "is number incorrect 1"
    if number_standard_landline(number) != "066":
        return "is lanline number incorrect "
    else:
        return "is number correct"