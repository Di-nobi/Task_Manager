from . import Base
from sqlalchemy import Column, String, Integer, LargeBinary
from sqlalchemy.orm import relationship
import uuid
import bcrypt
class User(Base):
    __tablename__ = 'user'
    id = Column(String(128), primary_key=True, nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(LargeBinary, nullable=False)
    tasks = relationship('Tasks', back_populates='user')

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.email = kwargs.get('email')
        self.password = self.__hash_password(kwargs.get('password'))
        
    def __hash_password(self, hash_password: str) -> bytes:
        """Hashes the password"""
        try:
            hash_salt = bcrypt.gensalt()
            encode_password = hash_password.encode('utf-8')
            return bcrypt.hashpw(encode_password, hash_salt)
        except Exception as err:
            print(f'Error occured at {err}')
    
    def valid_password(self, hash_password: str) -> bool:
        try:
            pw_d = hash_password.encode('utf-8')
            return bcrypt.checkpw(pw_d, self.password)
        except Exception as er:
            print(f'Error occured at {er}')