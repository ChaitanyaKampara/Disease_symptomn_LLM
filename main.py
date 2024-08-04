from fastapi import FastAPI, HTTPException, APIRouter
from contextlib import asynccontextmanager
from src.controllers.controllers import router

#lifecycle context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Symptom and Diagnoses API started.....")
    yield
    print("Symptom and Diagnoses API shutdown....")

app = FastAPI(title='Disease-Symptom-Diagnosis API', version='1.0.0', lifespan=lifespan)

app.include_router(router, prefix="/ddx")
