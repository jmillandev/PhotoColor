import pytest
from faker import Faker

from src.shared.infrastructure.dependency_injector import init as init_dependencies

init_dependencies()


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session")
def fake() -> Faker:
    return Faker()
