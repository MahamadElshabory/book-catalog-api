from passlib.context import CryptContext
from datetime import datetime , timedelta
from src.configg import Config
import jwt
import logging
from itsdangerous import URLSafeTimedSerializer
 

password_context = CryptContext ( schemes=['bcrypt'] )
ACCESS_TOKEN_EXPIRY = 3600

def generate_password_hash(password : str) -> str :
    
    hash = password_context.hash(password)
    return hash

def verify_password(password : str , hash : str) -> bool:
    
    return password_context.verify(password,hash)




def create_access_token(user_data: dict, expiry: timedelta = None):
    payload = {}

    payload["user"] = user_data

    if expiry is not None:
        payload["exp"] = datetime.now() + expiry
    else:
        payload["exp"] = datetime.now() + timedelta(seconds=ACCESS_TOKEN_EXPIRY)

    token = jwt.encode(
        payload=payload,
        key=Config.JWT_SECRET,
        algorithm=Config.JWT_ALGORITHM
    )

    return token


def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token,
            key=Config.JWT_SECRET,
            algorithms=[Config.JWT_ALGORITHM]
        )

        return token_data

    except jwt.PyJWTError as e:
        logging.exception(e)
        return None
    
def create_url_safe_token(data: dict):

    token = serializer.dumps(data)

    return token

def decode_url_safe_token(token:str):
    try:
        token_data = serializer.loads(token)

        return token_data
    
    except Exception as e:
        logging.error(str(e))