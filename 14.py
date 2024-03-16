from fastapi import FastAPI


app = FastAPI()


def validate_national_id(n):
    if len(str(n)) < 8 or len(str(n)) > 10:
        return False
    if len(str(n)) < 10:
        n_id = "0" * (10 - len(n) + n)
    coefficients = [10 , 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(int(n_id[i]) * coefficients[i] for i in range(9))
    reminder = total % 11
    if reminder < 2:
        return int(n_id[9]) == reminder
    else:
        return int(n_id[9]) == 11 - reminder


@app.post("/Home")
def code_melli(code_melli:int):
    if not validate_national_id(code_melli):
        return "code melli is incorrect"
    else:
        return "code melli is correct"