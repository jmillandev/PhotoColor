from uuid import UUID

from typing import Tuple
from fastapi.responses import StreamingResponse

from src.photo_stats.shower import PhotoStatsShower


async def show() -> Tuple[int, int, int]:
    shower = PhotoStatsShower()
    photo_stat = await shower()
    return (photo_stat.red, photo_stat.green, photo_stat.blue)
