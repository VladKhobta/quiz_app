import uvicorn

from fastapi import FastAPI, APIRouter

from api import question_router
import settings

app = FastAPI(
    title="Quiz Service",
)

main_api_router = APIRouter()

main_api_router.include_router(
    question_router,
    prefix="/questions",
    tags=["questions"]
)

app.include_router(main_api_router)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=settings.APP_PORT,
    )
