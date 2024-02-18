import pytest
from fastapi import status
from httpx import AsyncClient

from apps.config import settings

pytestmark = pytest.mark.anyio
from .factory import ColorPaletteFactory

class TestFindColorPaletteController:
    def setup_method(self):
        self._url = settings.API_PREFIX + "/image/%s/palette"

    async def test_success(self, client: AsyncClient) -> None:
        palette = await ColorPaletteFactory()

        response = await client.get(self._url % palette.photo_id )

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [
            palette.color1,
            palette.color2,
            palette.color3,
            palette.color4,
            palette.color5
        ]
