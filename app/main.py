# represent data structiures
# API routes:: register ,, login and sales

from fastapi import FastAPI

from app.schemas import (
    UserCreate,
    UserLogin
)

from app.auth import (
    register_user,
    login_user
)



app = FastAPI(
    title="Fashion Sales API"
)
#  Home Endpoint
@app.get("/")
def home():

    return {
        "message":
        "FastAPI Authentication Layer Running"
    }

# Register Endpoint

@app.post("/register")
def register(
    user: UserCreate
):

    return register_user(
        user.username,
        user.password
    )

@app.post("/login")
def login(
    user: UserLogin
):

    return login_user(
        user.username,
        user.password
    )

# addd imports
from app.dataset import (
       get_sales,
       get_summary
   )

# add endpoint

@app.get("/sales")
def sales():

    return get_sales()

# add endpoint

@app.get("/summary")
def summary():

    return get_summary()