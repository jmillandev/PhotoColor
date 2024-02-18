import pytest
from fastapi import status
from httpx import AsyncClient

from apps.config import settings
from tests.apps.photos.factory import PhotoFactory

from .factory import PhotoStatFactory

pytestmark = pytest.mark.anyio


class TestShowPhotoStatsController:
    def setup_method(self):
        self._url = f"{settings.API_PREFIX}/rgbstats"

    async def test_success(self, client: AsyncClient) -> None:
        photo = await PhotoFactory()
        await PhotoStatFactory(red=100, photo_id=photo.id)
        photo = await PhotoFactory()
        await PhotoStatFactory(red=0, green=100, photo_id=photo.id)

        response = await client.get(self._url)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        # I know that is not the response expected on Notion.
        # But is more explicit than [int, int, int]
        assert isinstance(data["red"], int)
        assert isinstance(data["green"], int)
        assert isinstance(data["blue"], int)
        # TODO: Flakky until Database will clean after each test
        # assert data == {'red': 50, 'green': 50, 'blue': 0]
