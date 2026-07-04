from sqlmodel.ext.asyncio.session import AsyncSession
from .models import User
from .schema import UserCreateModel
from .utils import generate_password_hash , verify_password
from sqlmodel import select

class UserService :
    
    async def get_user(self, email:str , session : AsyncSession):
        statement = select(User).where(User.email==email)
        result = await session.exec(statement)
        
        user = result.first()
        return user
    
    async def user_exist(self ,email:str , session : AsyncSession):
       user =  await self.get_user(email ,session)
       
       return True if user is not None else False
   
    async def create_user(self ,user_data : UserCreateModel , session : AsyncSession):
       
      user_data_dict = user_data.model_dump()
      # password = user_data_dict.pop("password")

      new_user = User (**user_data_dict) 
      
      new_user.password_hash = generate_password_hash(user_data_dict['password'])
      
      session.add(new_user)
      await session.commit()
      return new_user 
    
  
    """
    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):

        # convert to dict
        user_data_dict = user_data.model_dump()

        # ✅ extract password correctly
        password = user_data_dict.pop("password")

        # 🔥 DEBUG (just for now)
        print("PASSWORD:", password)
        print("LEN:", len(password))

        # ✅ build user manually (NO ** unpack)
        new_user = User(
            first_name=user_data_dict["first_name"],
            last_name=user_data_dict["last_name"],
            username=user_data_dict["username"],
            email=user_data_dict["email"],
            )

        # ✅ bcrypt safe guard
        password = str(password)[:72]

        new_user.password_hash = generate_password_hash(password)

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user
    """