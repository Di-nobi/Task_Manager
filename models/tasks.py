from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
class Tasks(Base):
    """Task Class Table"""
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, nullable=False)
    subject = Column(String(128), nullable=False)
    comment = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow())
    status = Column(String(128), default='pending')
    due_date = Column(String(128), nullable=True)
    user_id = Column(String(128), ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='tasks')

    def __init__(self, **kwargs):
        """Initalizes the class data"""
        # self.id = str(uuid.uuid4())
        self.subject = kwargs.get('subject')
        self.comment = kwargs.get('comment')
        self.status = kwargs.get('status')
        self.due_date = kwargs.get('due_date')
        self.user_id = kwargs.get('user_id')

    def to_dict(self):
        """Serializes the Instance of the class to a dictionary"""
        return {
            'id': self.id,
            'subject': self.subject,
            'comment': self.comment,
            'created_at': self.created_at.isoformat(),
            'status': self.status,
            'due_date': self.due_date,
            'user_id': self.user_id
        }