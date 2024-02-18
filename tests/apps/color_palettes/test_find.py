import pytest
from fastapi import status
from httpx import AsyncClient
from uuid import uuid4
from apps.config import settings

pytestmark = pytest.mark.anyio
from .factory import ColorPaletteFactory
from tests.apps.photos.factory import PhotoFactory

class TestFindColorPaletteController:
    def setup_method(self):
        self._url = settings.API_PREFIX + "/image/%s/palette"

    async def test_success(self, client: AsyncClient) -> None:
        photo = await PhotoFactory()
        palette = await ColorPaletteFactory(photo_id=photo.id)

        response = await client.get(self._url % palette.photo_id )

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [
            palette.color1,
            palette.color2,
            palette.color3,
            palette.color4,
            palette.color5
        ]

    async def test_return_not_found_error(self, client: AsyncClient) -> None:
        response = await client.get(self._url % uuid4())

        assert response.status_code == status.HTTP_404_NOT_FOUND
