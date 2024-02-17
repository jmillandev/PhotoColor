from fastapi import APIRouter, status

from .controllers import upload

router = APIRouter()


router.add_api_route(
    "/v1/upload",
    methods=["POST"],
    endpoint=upload,
    status_code=status.HTTP_201_CREATED,
)
