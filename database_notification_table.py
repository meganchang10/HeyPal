from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Notification(Base):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True)
    invite_count = (Integer)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship(User, foreign_keys=[user_id])

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'invite_count': self.invite_count,
        }


engine = create_engine('postgresql://heypal:PASSWORD@localhost/heypal')

Base.metadata.create_all(engine)












