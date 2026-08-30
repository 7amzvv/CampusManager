# CampusManager

API REST de gestion universitaire développée avec FastAPI et SQLite.

## Technologies

- Python 3.12
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn
- pytest

## Fonctionnalités

- Gestion complète des étudiants (CRUD)
- Gestion complète des cours (CRUD)
- Gestion complète des notes avec relations étudiant/cours (CRUD)
- Validation des données avec Pydantic
- Documentation automatique Swagger
- Tests automatisés avec pytest

## Architecture

```
CampusManager/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       ├── students.py
│       ├── courses.py
│       └── grades.py
├── tests/
│   └── test_students.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

```bash
git clone https://github.com/7amzvv/CampusManager.git
cd CampusManager
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Lancement

```bash
uvicorn app.main:app --reload
```

Accéder à la documentation : http://127.0.0.1:8000/docs

## Exemples de données

**Étudiant**
```json
{
  "first_name": "Hamza",
  "last_name": "Fadli",
  "email": "hamza@example.com"
}
```

**Cours**
```json
{
  "name": "Python",
  "description": "Programmation Python"
}
```

**Note**
```json
{
  "student_id": 1,
  "course_id": 1,
  "grade": 15.5
}
```

## Tests

```bash
pytest tests/ -v
```
