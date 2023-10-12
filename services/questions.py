import httpx
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from db.session import get_db
from db.dals import QuestionDAL
from schemas import QuestionPost, QuestionShow


DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


class QuestionService:

    def __init__(
            self,
            session: AsyncSession = Depends(get_db)
    ):
        self.session = session

    async def create(
            self,
            body: QuestionPost
    ) -> QuestionShow:
        question_count_left = body.count

        while question_count_left:  # cycle will work until required count of questions are saved to db
            print(question_count_left)
            response = await self.get_questions(question_count_left)

            for item in response:
                print(item["question"])
                # checking if question is already in database
                async with self.session.begin():
                    question_dal = QuestionDAL(self.session)
                    question = await question_dal.get_by_question(item["question"])
                    if not question:
                        datetime_obj = datetime.strptime(item["created_at"], DATE_FORMAT)
                        new_question = await question_dal.create(
                            question=item["question"],
                            answer=item["answer"],
                            creation_date=datetime_obj.date()
                        )
                        # question saved to db and minus one questions are left to response
                        question_count_left -= 1

        return QuestionShow(question=new_question.question)



    async def get_questions(
            self,
            count: int
    ):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://jservice.io/api/random?count={count}"
            )
            if response.status_code == 200:
                return response.json()

