from fastapi import APIRouter, status , Depends ,  Response
from datetime import datetime , timedelta
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from sqlmodel.ext.asyncio.session import AsyncSession
from .schema import UserCreateModel  , UserLoginModel , EmailModel , SignupResponseModel
from .service import UserService
from src.db.mainn import get_session
from .utils import decode_token , create_access_token , verify_password , create_url_safe_token , decode_url_safe_token
from src.celery_tasks import send_email
from src.celery_tasks import send_email


auth_router = APIRouter()
user_service = UserService()

REFRESH_TOKEN_EXPIRY = 2

@auth_router.post("/signup" , status_code=status.HTTP_201_CREATED ,response_model=SignupResponseModel ) 
async def create_user_account(user_data : UserCreateModel , session : AsyncSession = Depends(get_session)):
    
    email = user_data.email
    user_exist = await user_service.user_exist(email,session)
    if user_exist :
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="user exists already"
    )
    
    user = await user_service.create_user(user_data,session)
    
    body = f""" 
    <h1> welcome to the signup vverificattion</h1>
    <p> hello {user.first_name} , please confirm it is you to complete the signup process </p>
    
    """
    
    subject = "signup verification"
    
    task = send_email.delay( [user.email] , subject , body )
    
    return {
        
        "message": "Account created. Welcome email is being sent in the background.",
        "user": user,
        "email_task_id": task.id
    
    }
    



@auth_router.post("/login")
async def login_user(
    login_data: UserLoginModel,
    session: AsyncSession = Depends(get_session)
):
    email = login_data.email
    password = login_data.password

    user = await user_service.get_user(email, session)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    password_valid = verify_password(password, user.password_hash)

    if not password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        user_data={
            "email": user.email,
            "user_id": user.id
        }
    )

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username
        }
    }
    
    raise InvalidCredentials()
     
@auth_router.post("/verification_email")
async def send_verification_email(email : EmailModel, session: AsyncSession = Depends(get_session)):
    
    body = "<h1> this is the verf email </h1>"
    subject = " verification email "
    
    task = send_email.delay(email.addresses , subject , body)
    
    return {
        "message": "Email task sent to Celery",
        "task_id": task.id
    }
     