from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_tables():
    Base.metadata.create_all(bind = engine)

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title = settings.PROJECT_NAME, version = settings.PROJECT_VERSION)
    origins = [
        "*"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    create_tables()
    include_router(app)
    return app


app = start_application()


