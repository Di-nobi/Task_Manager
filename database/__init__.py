from .db import database

store = database()
store.begin_session()