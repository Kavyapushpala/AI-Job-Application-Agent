from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime

from database.base import Base


class Resume(Base):

    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String(255), nullable=False)

    name = Column(String(255))

    email = Column(String(255))

    phone = Column(String(50))

    skills = Column(Text)

    education = Column(Text)

    projects = Column(Text)

    experience = Column(Text)

    certifications = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )