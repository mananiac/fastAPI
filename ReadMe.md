Windows installation 

- Python 3.12
    Download .exe from offical docs & run it

- Upgrading pip [not required]
    `py -m pip install --upgrade pip setuptools wheel`

- Installing fastapi
    `py -m pip install "fastapi"`

- Installing uvicorn [ASGI server]
    `py -m pip install "uvicorn[standard]"`

- Installing SQLAlchemy [ORM]
    `py -m pip install "sqlalchemy"`

- Installing Alembic [ Data Migration ]
    `py -m pip install alembic`     
    `py -m alembic init alembic`

Mac installation 

- Python 3.12
    Download .exe from offical docs & run it

- Installing fastapi
    `pip install "fastapi"`

- Installing uvicorn [ASGI server]
    `pip install "uvicorn[standard]"`

- Installing SQLAlchemy [ORM]
    `py -m pip install "sqlalchemy"`

- Installing Alembic [ Data Migration ]
    `pip install alembic`    
    `alembic init alembic`

Directory Structure    

    fastAPI
        ├──ReadMe.md
        └──CRUD-APIs
            └──fastAPI-best-practices
                ├──__init__.py
                ├── crud.py
                ├── database.py
                ├── main.py
                ├── models.py
                └── schemas.py
            └──CRUD-APIs
                ├── database.py
                ├── main.py
                └── models.py
            └──chatApp
                └── main.py
            └──realTimeChatServer
                ├── main.py
                └── templates
                    ├── homepage.html
                    └── base.html         