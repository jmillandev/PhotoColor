from uuid import UUID

import pytest
from fastapi import status
from httpx import AsyncClient
from unittest.mock import patch

from apps.config import settings

pytestmark = pytest.mark.anyio
from src.photos.entity import Photo
from src.color_palettes.entity import ColorPalette
from src.photo_stats.entity import PhotoStat

class TestUploadPhotoController:
    def setup_method(self):
        self._url = f"{settings.API_PREFIX}/upload"
        self.asset = (
            "sample.jpg",
            open("tests/fixtures/images/sample.jpg", "rb"),
            "image/jpeg",
        )

    async def test_success(self, client: AsyncClient) -> None:
        response = await client.post(self._url, files={"asset": self.asset})

        assert response.status_code == status.HTTP_201_CREATED, response.text
        photo_id = UUID(response.json())

        assert await Photo.find(photo_id) is not None

    @patch.object(ColorPalette, 'save')
    @patch.object(PhotoStat, 'save')
    async def test_color_palette_and_stats_should_be_saved(self, save_color_palette, save_photo_stat, client: AsyncClient) -> None:
        await client.post(self._url, files={"asset": self.asset})

        assert save_color_palette.called
        assert save_photo_stat.called
