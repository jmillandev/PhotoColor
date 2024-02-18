import pytest
from fastapi import status
from httpx import AsyncClient

from apps.config import settings
from uuid import uuid4

pytestmark = pytest.mark.anyio
from .factory import PhotoFactory

class TestFindPhotoController:
    def setup_method(self):
        self._url = f"{settings.API_PREFIX}/image/%s"
        with open("tests/fixtures/images/sample.jpg", "rb") as f:
            self.asset = f.read()

    async def test_success(self, client: AsyncClient) -> None:
        photo = await PhotoFactory(asset=self.asset)
        response = await client.get(self._url % photo.id)

        assert response.status_code == status.HTTP_200_OK
        asset = response.read()
        assert isinstance(asset, bytes)
        assert asset == self.asset

    async def test_return_not_found_error(self, client: AsyncClient) -> None:
        response = await client.get(self._url % uuid4())

        assert response.status_code == status.HTTP_404_NOT_FOUND
