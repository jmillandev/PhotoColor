from uuid import uuid4

import pytest
from fastapi import status
from httpx import AsyncClient

from apps.config import settings
from src.color_palettes.entity import ColorPalette
from src.photos.entity import Photo
from tests.apps.color_palettes.factory import ColorPaletteFactory

from .factory import PhotoFactory

pytestmark = pytest.mark.anyio


class TestFindPhotoController:
    def setup_method(self):
        self._url = f"{settings.API_PREFIX}/image/%s/delete"
        with open("tests/fixtures/images/sample.jpg", "rb") as f:
            self.asset = f.read()

    async def test_success(self, client: AsyncClient) -> None:
        photo = await PhotoFactory(asset=self.asset)
        await ColorPaletteFactory(photo_id=photo.id)
        response = await client.post(self._url % photo.id)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.text == ""

        # TODO: Remove this assert when add Test Cases to Delete Application Service
        assert await Photo.find(photo.id) is None  # type: ignore[misc, arg-type]
        # TODO: Remove this assert when implement EventBus
        assert await ColorPalette.find_by_photo_id(photo.id) is None  # type: ignore[misc, arg-type]

    async def test_return_204_if_not_found_resource(self, client: AsyncClient) -> None:
        response = await client.post(self._url % uuid4())

        assert response.status_code == status.HTTP_204_NO_CONTENT
