from models.tasks import Tasks
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models import Base
class database:
    """
    Defines the SQL database ORM.

    This class handles the connection to a PostgreSQL database using SQLAlchemy.
    It sets up the engine and metadata for the ORM and provides methods to
    start a session and save changes to the database.
    """
    def __init__(self):
        """
        Initializes the database engine and creates all tables.

        This constructor creates a SQLAlchemy engine for the SQL LITE database
        using the provided connection string. It also creates all tables defined
        in the metadata.
        """
        self.__engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.create_all(self.__engine)
        # self.__session = None
    def begin_session(self):
        """
        Starts the database session.

        This method initializes the database session by creating a session factory 
        using SQLAlchemy's sessionmaker, binding it to the engine, and setting 
        expire_on_commit to True. It then sets the scoped session as an instance 
        attribute for managing the session.

        Attributes:
            __engine: The SQLAlchemy engine to bind the session to.
            __session: The scoped session created by the session factory.
        """
        sess_fac = sessionmaker(bind=self.__engine, expire_on_commit=True)
        self.__session = scoped_session(sess_fac)

    def end_session(self):
        """Closes the session"""
        self.__session.remove()

    def save(self):
        """
        Commits the current transaction to the database.

        This method commits all the changes made during the current session to the
        database. It ensures that all operations performed within the session are 
        saved permanently.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the database.

        This method removes the specified object from the current session. 
        The changes will be committed to the database upon calling the save method.

        Args:
            obj (object): The SQLAlchemy model instance to be deleted.
        """
        self.__session.delete(obj)

    def get_usr(self, id):
        """
        Retrieves a user by their ID.

        This method queries the database for a user with the specified ID. If the user
        is found, it returns the user object; otherwise, it returns None.

        Args:
            id (str): The ID of the user to retrieve.

        Returns:
            User: The user object if found, None otherwise.
        """
        user = self.__session.query(User).filter(User.id == id).first()
        if not user:
            return None
        return user
    
    def get_task(self, id):
        """
        Retrieves a task by its ID.

        This method queries the database for a task with the specified ID. If the task
        is found, it returns the task object; otherwise, it returns None.

        Args:
            id (str): The ID of the task to retrieve.

        Returns:
            Tasks: The task object if found, None otherwise.
        """
        tasks = self.__session.query(Tasks).filter(Tasks.id == id).first()
        if not tasks:
            return None
        return tasks
    
    def usr_email(self, email: str):
        """
        Retrieves a user by their email.

        This method queries the database for a user with the specified email. If the user
        is found, it returns the user object; otherwise, it returns None.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            User: The user object if found, None otherwise.
        """
        em = self.__session.query(User).filter(User.email == email).first()
        if not em:
            return None
        return em
    
    def reg_user(self, **kwargs):
        """
        Registers a new user in the database.

        Parameters:
        - **kwargs: Keyword arguments representing user attributes.

        Returns:
        - new_user: Newly created User object.

        This method creates a new User object using the provided keyword arguments,
        adds it to the session, and commits the changes to the database.
        """
        new_user = User(**kwargs)
        self.__session.add(new_user)
        self.__session.commit()
        return new_user
    
    def get_tasks(self):
        """
        Retrieves all tasks from the database.

        Returns:
        - all_tasks: A list of all Task objects in the system, or None if no tasks are found.

        This method queries the database session for all Task objects and returns them as a list.
        If no tasks are found, it returns None.
        """
        all_tasks = self.__session.query(Tasks).all()
        if not all_tasks:
            return None
        return all_tasks
    
    def add_task(self, **kwargs):
        """
        Adds a new task to the database.

        Parameters:
        - **kwargs: Keyword arguments representing task attributes.

        Returns:
        - a_task: Newly created Task object.

        This method creates a new Task object using the provided keyword arguments,
        adds it to the session, and commits the changes to the database.
        """
        a_task = Tasks(**kwargs)
        self.__session.add(a_task)
        self.__session.commit()
        return a_task