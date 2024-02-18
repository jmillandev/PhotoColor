from fastapi import APIRouter, status

from .controllers import show

router = APIRouter()


router.add_api_route(
    "/rgbstats",
    methods=["GET"],
    endpoint=show,
    status_code=status.HTTP_200_OK
)
