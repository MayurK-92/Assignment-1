from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def read_root():
    return {"Hello": "MCC Students!!!"}

@app.get("/about")
def about():
    return {"msg": "About Us"}

@app.get("/courses")
def get_courses():
    courses = [
        {"id": 1, "name": "DevOps", "instructor": "Dr.Jyotika Chheda"},
        {"id": 2, "name": "Internet of Things", "instructor": "Dr.Hiren Dand"},
        {"id": 3, "name": "Big Data and NOSQL ", "instructor": "Dr.Vishal Borude"},
        {"id": 4, "name": "Artificial Intelligence", "instructor": "Dr.Priti Pathak"}
    ]
    return {"courses": courses}