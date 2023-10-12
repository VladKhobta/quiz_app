from typing import Optional
import re
from uuid import UUID
from datetime import datetime

from fastapi import HTTPException

from pydantic import BaseModel


class TunedModel(BaseModel):

    class Config:
        from_attributes = True


class QuestionPost(BaseModel):
    count: int


class QuestionShow(TunedModel):
    question: Optional[str]
