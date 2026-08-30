from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None

class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    model_config = {"from_attributes": True}


class CourseCreate(BaseModel):
    name: str
    description: Optional[str] = None

class CourseUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CourseResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    model_config = {"from_attributes": True}


class GradeCreate(BaseModel):
    student_id: int
    course_id: int
    grade: float

    @field_validator("grade")
    @classmethod
    def validate_grade(cls, value):
        if value < 0 or value > 20:
            raise ValueError("La note doit être comprise entre 0 et 20")
        return value

class GradeUpdate(BaseModel):
    grade: float

    @field_validator("grade")
    @classmethod
    def validate_grade(cls, value):
        if value < 0 or value > 20:
            raise ValueError("La note doit être comprise entre 0 et 20")
        return value

class GradeResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    grade: float

    model_config = {"from_attributes": True}