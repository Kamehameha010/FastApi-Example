

from fastapi import FastAPI

from routes.users import user_router as users



app = FastAPI()

app.include_router(users, prefix="/api/v1")
