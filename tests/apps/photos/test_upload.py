from uuid import UUID

import pytest
from faker import Faker
from fastapi import status
from httpx import AsyncClient

from apps.config import settings

fake = Faker()

pytestmark = pytest.mark.anyio


class TestUploadPhotoController:
    def setup_method(self):
        self._url = f"{settings.API_PREFIX}/v1/upload"
        self.asset = (
            "sample.jpg",
            open("tests/fixtures/images/sample.jpg", "rb"),
            "image/jpeg",
        )

    async def test_success(self, client: AsyncClient) -> None:
        response = await client.post(self._url, files={"asset": self.asset})

        assert response.status_code == status.HTTP_201_CREATED, response.text
        UUID(response.json())
