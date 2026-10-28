# Handles bcrypt hashing//JWT creation??JWT verififcation

from  datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "fashion_secret_key"

ALGORITHM = "HS256"

ACCESS_TOKEN_MINUTES = 30


pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)


#--Password hashing

def hash_password(password: str):

    print("VALUE:", password)
    print("TYPE:", type(password))
    print("LEN:", len(password))

    password = password[:72]
    return pwd_context.hash(password)

def verify_password(
        plain_password:str,
        hashed_password:str
):
    plain_password = plain_password[:72]
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

# JWT creation

def create_access_token(data: dict):

    to_encode  = data.copy()

    expire  = datetime.utcnow()  + timedelta(
        minutes=ACCESS_TOKEN_MINUTES
    )

    to_encode.update(
        {"exp": expire}
    )

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt