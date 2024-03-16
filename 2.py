from fastapi import FastAPI


app = FastAPI()


def check_farsi_name(n):
    for char in n:
        if '\u0600' <= char <= '\u06FF':
            continue 
        else:
            return False  
    return True 

@app.post("/home")
def main(name : str):   
    if not check_farsi_name(name):
        return "All letters must be Farsi or Do not contain special symbols or numbers"
    elif len(name) > 10:
        return "The maximum string length must be ten"
    return f"name is : {name}"