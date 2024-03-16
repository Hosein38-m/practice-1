from fastapi import FastAPI


app = FastAPI()
def college_trust(n):
    lst_college = ["فنی و مهندسی", "علوم پایه", "علوم انسانی", "دامپزشکی", "اقتصاد", "کشاورزی", "منابع طبیعی"]
    for lst in lst_college:
        if n in lst:
            return True

@app.post("/Home")
def college(name_college: str):
    if college_trust(name_college):
        return "name college is true"
    else:
        return "is value incorrect"
    
    