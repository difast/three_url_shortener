from fastapi import FastAPI
from app.routers import urls
from app.database import Base, engine

app = FastAPI()
app.include_router(urls.router)

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)