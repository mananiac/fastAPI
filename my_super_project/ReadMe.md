Windows installation 

- Python 3.12
    Download .exe from offical docs & run it

- Upgrading pip [not required]
    py -m pip install --upgrade pip setuptools wheel

- Installing fastapi
    py -m pip install "fastapi"

- Installing uvicorn [ASGI server]
    py -m pip install "uvicorn[standard]"

- Installing SQLAlchemy [ORM]
    py -m pip install "sqlalchemy"


Directory Structure    

my_super_app
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    └── schemas.py
