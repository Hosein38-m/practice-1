from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import jdatetime
import json


class item(BaseModel):
    studend_number: int
    name: str
    date: str
    letter_of_series_number: str
    Birth_certificate_seriesnumber: int
    number_of_series_number: int
    province: str
    city: str
    address: str
    postal_code: int
    phone_number: str | None = None
    landline_number: str | None = None
    name_college: str
    Field_of_Study:str
    marital_statusn: str
    code_melli:int


def split_number(n):
    if len(str(n)) == 11:
        n_str = str(n)[0:3]
        return int(n_str)
    else:
        return False

def Fixed_field(n):
    if len(str(n)) == 11:
        n_str = str(n)[3:9]
        return int(n_str)
    else:
        return False
def index(n):
    if len(str(n)) == 11:
        n_str = str(n)[9:11]
        return int(n_str)
    else:
        return False


def check_farsi_name(n):
    for char in n:
        if '\u0600' <= char <= '\u06FF':
            continue 
        else:
            return False  
    return True 

def check_shamsi(d_str):
    obj_date = jdatetime.datetime
    try:
        obj_date.strptime(d_str, '%Y/%m/%d')
        return True
    except ValueError:
        return False

def is_center(n):
    with open("iran_provinces.json", "r", encoding= "utf-8") as f:
        ob = json.load(f)
    for char in ob:
        if char in n:
            return True
        
def is_cities(n):
    with open("province.json", "r", encoding="utf-8") as f:
        ob = json.load(f)

    for char in ob:
        if char in n:
            return True

def number_standard(n):
    return n[0:2]

def number_standard_landline(n):
    return n[0:3]

def college_trust(n):
    lst_college = ["فنی و مهندسی", "علوم پایه", "علوم انسانی", "دامپزشکی", "اقتصاد", "کشاورزی", "منابع طبیعی"]
    for lst in lst_college:
        if n in lst:
            return True

def trust(n):
    with open("engineering_fields.json", "r", encoding= "utf-8") as f:
        ob = json.load(f)
    for char in ob :
        if n in char:
            return True
        
def validate_national_id(n):
    if len(str(n)) < 8 or len(str(n)) > 10:
        return False
    if len(str(n)) < 10:
        n_id = "0" * (10 - len(str(n)) + n)
    if len(str(n)) == 10:
        n_id = str(n)
    coefficients = [10 , 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(int(n_id[i]) * coefficients[i] for i in range(9))
    reminder = total % 11
    if reminder < 2:
        return int(n_id[9]) == reminder
    else:
        return int(n_id[9]) == 11 - reminder


app = FastAPI()
@app.post("/Home")
async def check(it: item):
    errors = {}
    try:
        item_data = it.dict()
    except ValidationError as e:
        # Collect validation errors
        for error in e.errors():
            field = error["loc"][0]
            errors[field] = error["msg"]
    if len(str(it.studend_number)) != 11:
        errors["studend_number"] = "The number of digits entered is incorrect"
    if not 402 >= split_number(it.studend_number) >= 400 :
        errors["split_number"] = "The year field is incorrect"
    if Fixed_field(it.studend_number) != 114150:
        errors["student_number"] = "The fixed field is wrong"
    if not 99 >= index(it.studend_number) >= 1:
        errors["student_number"] = "The index part is wrong"
    if not check_farsi_name(it.name):
        errors["name"] = "All letters must be Farsi or Do not contain special symbols or numbers"
    if len(it.name) > 10:
        errors["name"] = "The maximum string length must be ten"
    if not check_shamsi(it.date) == True:
        errors["date"] = "This date is incorrect"
    if len(it.letter_of_series_number) > 3 and check_farsi_name(it.letter_of_series_number) == False:
        errors["letter_of_series_number"] = "The letter part of the birth certificate was entered incorrectly"
    if len(str(it.Birth_certificate_seriesnumber)) > 2:
        errors["birth_certificate_seriesnumber"] = "The numeric part of the birth certificate series was entered incorrectly"
    if len(str(it.number_of_series_number)) > 6:
        errors["number_of_series_number"] = "The serial number of the birth certificate was entered incorrectly"
    if not is_center(it.province) == True:
        errors["center"] = "incorrect province" 
    if 100 < len(it.address):
        errors["address"] = "address incorrectly" 
    if len(str(it.postal_code)) != 10:
        errors["postal_code"] = "postal code is invalued"
    if len(it.phone_number) != 11:
        errors["phone_number"] = "Mobile phone number must be 11 digits"
    if number_standard(it.phone_number) != "09":
        errors["phone_number"] = "is phone number incorrect "  
    if len(it.landline_number) != 11:
        errors["landline_number"] = "landline number must be 11 digits"
    if number_standard_landline(it.landline_number) != "066":
        errors["landline_number"] = "is landline number incorrect " 
    if not college_trust(it.name_college):
        errors["name_college"] = "name college is wrong"  
    if not trust(it.Field_of_Study) == True:
        errors["field_study"] = "field of study is wrong" 
    if not (it.marital_statusn == "married" or it.marital_statusn == "single"):
        errors["marital"] = "is marital status is wrong value"
    if not validate_national_id(it.code_melli):
        errors["code_melli"] = "code melli is incorrect"
    if errors:
        raise HTTPException(status_code = 422, detail={"detail": "Validation error", "errors": errors})
    else:
        return it