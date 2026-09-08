from fastapi import FastAPI
from app.models import models
from app.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)