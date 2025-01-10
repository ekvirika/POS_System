import pytest
from fastapi.testclient import TestClient
from app.main import create_app
from app.db.database import Base, engine, SessionLocal

@pytest.fixture(scope="module")
def test_app():
    """
    Fixture to create a FastAPI test application with a fresh database.
    """
    Base.metadata.create_all(bind=engine)  # Create tables
    app = create_app()
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)  # Drop tables after tests

@pytest.fixture(scope="function")
def db_session():
    """
    Fixture to provide a fresh database session for each test.
    """
    session = SessionLocal()
    yield session
    session.close()
