from fastapi import APIRouter, status

from .controllers import upload, find, delete

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

router.add_api_route(
    "/image/{id}/delete",
    methods=["POST"],
    endpoint=delete,
    status_code=status.HTTP_204_NO_CONTENT,
)
