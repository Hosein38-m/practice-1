from fastapi import FastAPI


app = FastAPI()


def number_standard(n):
    return n[0:2]


@app.post("/Home")
def Phone_number(number):
    if len(number) != 11:
        return "Mobile phone number must be 11 digits"
    if number_standard(number) != "09":
        return "is phone number incorrect "
    else:
        return "is number correct"
    