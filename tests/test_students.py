import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_create_student():
    response = client.post("/students/", json={
        "first_name": "Hamza",
        "last_name": "Fadli",
        "email": "hamza@example.com"
    })
    assert response.status_code == 201
    assert response.json()["first_name"] == "Hamza"

def test_read_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_student_not_found():
    response = client.get("/students/999")
    assert response.status_code == 404

def test_update_student():
    client.post("/students/", json={
        "first_name": "Hamza",
        "last_name": "Fadli",
        "email": "hamza@example.com"
    })
    response = client.put("/students/1", json={"first_name": "Youssef"})
    assert response.status_code == 200
    assert response.json()["first_name"] == "Youssef"

def test_delete_student():
    client.post("/students/", json={
        "first_name": "Hamza",
        "last_name": "Fadli",
        "email": "hamza@example.com"
    })
    response = client.delete("/students/1")
    assert response.status_code == 204

def test_invalid_grade():
    response = client.post("/grades/", json={
        "student_id": 1,
        "course_id": 1,
        "grade": 25
    })
    assert response.status_code == 422