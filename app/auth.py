#Business logic

from fastapi import HTTPException

from app.fake_db import users_db

from app.security import (
    hash_password,
    verify_password,
    create_access_token
)

def register_user(username, password):

    print("USERNAME:", username)
    print("PASSWORD:", password)
    print("TYPE:", type(password))
    print("LENGTH:", len(password))

    hashed = hash_password(password)

    users_db[username] = {

        "username": username,

        "password": hashed
    }

    return {
        "message": "User created successfully"
    }


# Login

def  login_user(
        username,
        password
):
    user = users_db.get(username)

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        password,
        user["password"]
    ):
        raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
         )

    token = create_access_token(
        {"sub": username}
    )

    return {
        "access_token": token,
        
        "token_type": "bearer"
    }