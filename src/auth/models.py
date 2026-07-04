from sqlmodel import SQLModel, Field
from datetime import datetime



class User (SQLModel,table=True) :
    id : int | None = Field(default=None, primary_key=True)
    username : str
    email : str 
    first_name : str
    last_name : str
    is_verified : bool = False
    password_hash : str = Field(exclude=True)
    created_at : datetime = Field(default_factory=datetime.now)
    updated_at : datetime = Field(default_factory=datetime.now)
    
    
    
def __repr__(self):
        return f"<User {self.username}>"