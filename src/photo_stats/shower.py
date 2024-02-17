from uuid import UUID

from kink import inject

from .entity import PhotoStat


@inject(use_factory=True)
class PhotoStatsShower:
    # TODO: Inject PhotoStatRepository

    async def __call__(self, photo_id: UUID) -> PhotoStat:
        return await PhotoStat.avg(photo_id)
