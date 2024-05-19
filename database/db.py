from models.tasks import Tasks
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models import Base
class database:
    """Defines the SQL database orm"""
    def __init__(self):
        self.__engine = create_engine("postgresql+psycopg2://dwayne:Dinobi_1122@localhost:5432/niyo", echo=False)
        Base.metadata.create_all(self.__engine)
        # self.__session = None
    def begin_session(self):
        """"Starts the database"""
        sess_fac = sessionmaker(bind=self.__engine, expire_on_commit=True)
        self.__session = scoped_session(sess_fac)

    def end_session(self):
        """Closes the session"""
        self.__session.remove()

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        self.__session.delete(obj)

    def get_usr(self, id):
        user = self.__session.query(User).filter(User.id == id).first()
        if not user:
            return None
        return user
    
    def get_task(self, id):
        tasks = self.__session.query(Tasks).filter(Tasks.id == id).first()
        if not tasks:
            return None
        return tasks
    
    def usr_email(self, email):
        em = self.__session.query(User).filter(User.email == email).first()
        if not em:
            return None
        return em
    
    def reg_user(self, **kwargs):
        new_user = User(**kwargs)
        self.__session.add(new_user)
        self.__session.commit()
        return new_user
    
    def get_tasks(self):
        all_tasks = self.__session.query(Tasks).all()
        if not all_tasks:
            return None
        return all_tasks
    
    def add_task(self, **kwargs):
        a_task = Tasks(**kwargs)
        self.__session.add(a_task)
        self.__session.commit()
        return a_task