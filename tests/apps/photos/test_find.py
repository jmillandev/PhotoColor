import pytest
from fastapi import status
from httpx import AsyncClient

from apps.config import settings

pytestmark = pytest.mark.anyio
from .factory import PhotoFactory

class TestFindPhotoController:
    def setup_method(self):
        self._url = f"{settings.API_PREFIX}/image/"
        with open("tests/fixtures/images/sample.jpg", "rb") as f:
            self.asset = f.read()

    async def test_success(self, client: AsyncClient) -> None:
        photo = await PhotoFactory(asset=self.asset)
        response = await client.get(self._url + str(photo.id))

        assert response.status_code == status.HTTP_200_OK
        asset = response.read()
        assert isinstance(asset, bytes)
        assert asset == self.asset
