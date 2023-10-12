from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from schemas import QuestionPost, QuestionShow
from services import QuestionService

question_router = APIRouter()


@question_router.post("/")
async def question_post(
        body: QuestionPost,
        question_service: QuestionService = Depends()
) -> QuestionShow:
    if body.count < 0 or body.count > 100:
        # handling wrong input data case
        raise HTTPException(
            status_code=422,
            detail="The number of questions should be greater than zero and less than one hundred"
        )
    last_saved_question = await question_service.create(body)
    return last_saved_question
