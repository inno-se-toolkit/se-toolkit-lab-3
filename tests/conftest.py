import os
import pytest
from fastapi.testclient import TestClient

os.environ["API_TOKEN"] = "my-secret-api-key"
os.environ["POSTGRES_HOST_PORT"] = "42002"
os.environ["POSTGRES_DB"] = "lab3"
os.environ["POSTGRES_USER"] = "postgres"
os.environ["POSTGRES_PASSWORD"] = "postgres"
os.environ["DATABASE_URL"] = "postgresql+asyncpg://postgres:postgres@localhost:42002/lab3"

from app.main import app 

@pytest.fixture(scope="session")
def client():
    with TestClient(app) as c:
        yield c