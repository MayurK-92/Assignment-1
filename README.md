
# Git Branching and Workflow

This repository demonstrates a Git branching strategy for a Python project, utilizing feature branches, release branches, and tagging.

## Prerequisites

- Git installed on your machine
- A GitHub (or other Git service) account
- A sample Python project (e.g., a Flask or FastAPI application)

## Steps

### 1. Repository Setup

#### 1.1 Create a New Git Repository

If you don't have an existing repository, create a new one:

1. Navigate to your GitHub account and create a new repository.
2. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   cd <your-repository>
   ```

#### 1.2 Initialize and Push Sample Project

If you have a sample project, initialize Git and push it to the repository:
#### Sample code:
```python
# In your Flask app file (e.g., app.py)
from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def read_root():
    return {"Hello": "MCC Students!!!"}

@app.get("/about")
def about():
    return {"msg": "About Us"}

```
#### Push commands

```bash
git init
git add .
git commit -m "Initial commit with sample project"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repository>.git
git push -u origin main
```

### 2. Create Feature Branch

#### 2.1 Create and Switch to the Feature Branch

Create a new branch named `feature/new-feature` from the `main` branch:

```bash
git checkout -b feature/new-feature
```

#### 2.2 Implement a New Feature

Add your new feature to the project. For example, add a new endpoint to a Flask app:

```python
# In your Flask app file (e.g., app.py)
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
```

#### 2.3 Commit and Push the Changes

```bash
git add .
git commit -m "Add new feature endpoint"
git push origin feature/new-feature
```

### 3. Create Release Branch

#### 3.1 Create and Switch to the Release Branch

Create a release branch named `release/v1.0.0` from the `main` branch:

```bash
git checkout main
git checkout -b release/v1.0.0
```

#### 3.2 Merge Feature Branch into Release Branch

Merge the `feature/new-feature` branch into the `release/v1.0.0` branch:

```bash
git merge feature/new-feature
```

Resolve any merge conflicts if they occur, then commit the changes.

#### 3.3 Tag the Release

Tag the release branch with `v1.0.0`:

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
```

#### 3.4 Push the Release Branch and Tag

```bash
git push origin release/v1.0.0
git push origin v1.0.0
```

## Conclusion

You have successfully implemented a branching strategy in Git, including creating feature branches, release branches, and tagging a release. 

---

Replace `<your-username>` and `<your-repository>` with the appropriate values specific to your GitHub account and repository name.
