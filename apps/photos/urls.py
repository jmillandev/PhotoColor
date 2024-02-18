from fastapi import APIRouter, status

from .controllers import upload, find

router = APIRouter()


router.add_api_route(
    "/upload",
    methods=["POST"],
    endpoint=upload,
    status_code=status.HTTP_201_CREATED,
)

router.add_api_route(
    "/image/{id}",
    methods=["GET"],
    endpoint=find,
    status_code=status.HTTP_200_OK,
)
