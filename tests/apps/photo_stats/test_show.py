import pytest
from fastapi import status
from httpx import AsyncClient

from apps.config import settings

pytestmark = pytest.mark.anyio
from .factory import PhotoStatFactory

class TestShowPhotoStatsController:
    def setup_method(self):
        self._url = f"{settings.API_PREFIX}/rgbstats"

    @pytest.mark.skip('Flakky until Database will clean after each test')
    async def test_success(self, client: AsyncClient) -> None:
        await PhotoStatFactory(red=100)
        await PhotoStatFactory(red=0, green=100)

        response = await client.get(self._url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [50, 50, 0]
