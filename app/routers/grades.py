from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/grades", tags=["Notes"])

@router.get("/", response_model=list[schemas.GradeResponse])
def read_grades(db: Session = Depends(get_db)):
    return crud.get_grades(db)

@router.get("/{grade_id}", response_model=schemas.GradeResponse)
def read_grade(grade_id: int, db: Session = Depends(get_db)):
    grade = crud.get_grade(db, grade_id)
    if not grade:
        raise HTTPException(status_code=404, detail="Note introuvable")
    return grade

@router.post("/", response_model=schemas.GradeResponse, status_code=201)
def create_grade(grade: schemas.GradeCreate, db: Session = Depends(get_db)):
    student = crud.get_student(db, grade.student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    course = crud.get_course(db, grade.course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Cours introuvable")
    return crud.create_grade(db, grade)

@router.put("/{grade_id}", response_model=schemas.GradeResponse)
def update_grade(grade_id: int, grade: schemas.GradeUpdate, db: Session = Depends(get_db)):
    updated = crud.update_grade(db, grade_id, grade)
    if not updated:
        raise HTTPException(status_code=404, detail="Note introuvable")
    return updated

@router.delete("/{grade_id}", status_code=204)
def delete_grade(grade_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_grade(db, grade_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note introuvable")