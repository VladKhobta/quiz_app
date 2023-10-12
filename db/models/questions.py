from db.models import Base

from sqlalchemy import Column
from sqlalchemy import String, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid


class QuestionModel(Base):

    __tablename__ = "questions"

    question_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    question = Column(
        String,
        nullable=False,
        unique=True
    )
    answer = Column(
        String,
        nullable=False,
        unique=False
    )
    creation_date = Column(
        Date,
        nullable=False
    )
