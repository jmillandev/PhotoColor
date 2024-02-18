from fastapi import APIRouter, status

from .controllers import find

router = APIRouter()


router.add_api_route(
    "/image/{photo_id}/palette",
    methods=["GET"],
    endpoint=find,
    status_code=status.HTTP_200_OK,
)
