import datetime
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db.models import QuestionModel



class QuestionDAL:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def create(
            self,
            question: str,
            answer: str,
            creation_date: datetime.date
    ) -> QuestionModel:
        new_question = QuestionModel(
            question=question,
            answer=answer,
            creation_date=creation_date
        )
        self.session.add(new_question)
        await self.session.flush()
        return new_question


    async def get_by_question(
            self,
            question: str
    ) -> Optional[QuestionModel]:
        query = (
            select(QuestionModel)
            .where(QuestionModel.question == question)
        )
        res = await self.session.execute(query)

        return res.scalar()
