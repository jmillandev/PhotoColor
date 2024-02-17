"""All infrastructure dependencies should be imported here. This file is used to
initialize the dependency injector.

Infracstructure dependencies need to be imported here for python interpreter to know about
them. This is necessary because the dependency injector uses the `importlib` module to
import the dependencies.
"""

from os import makedirs

from kink import Container, di
from libcloud.storage.drivers.local import LocalStorageDriver
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_file.storage import StorageManager

from src.shared.infrastructure.persistence.sqlalchemy.session import SqlAlchemySession


def init(dependency_injector: Container = di) -> None:
    dependency_injector.factories[type[AsyncSession]] = lambda _: SqlAlchemySession  # type: ignore[misc]  # noqa: E501

    # Configure Storage
    makedirs("./files/photos", 0o777, exist_ok=True)
    container = LocalStorageDriver("./files").get_container("photos")
    try:
        StorageManager.add_storage("photos", container)
    except RuntimeError:
        pass
