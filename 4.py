from fastapi import FastAPI


def check_farsi_name(n):
    for char in n:
        if '\u0600' <= char <= '\u06FF':
            continue 
        else:
            return False  
    return True 


app = FastAPI()


@app.post("/Home")
def series_birth_certificate(letter: str, Birth_certificate_seriesnumber: int, number: int):
    if len(letter) > 3 and check_farsi_name(letter) == False:
        return "The letter part of the birth certificate was entered incorrectly"
    if len(str(Birth_certificate_seriesnumber)) > 2:
        return "The numeric part of the birth certificate series was entered incorrectly"
    if len(str(number)) > 6:
        return "The serial number of the birth certificate was entered incorrectly"
    else:
        return "The serial number of the birth certificate is correct"