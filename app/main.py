from fastapi import FastAPI
from app.database import engine, Base
from app.routers import students, courses, grades

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CampusManager",
    description="API REST de gestion des étudiants, cours et notes",
    version="1.0.0"
)

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(grades.router)