from uuid import UUID

from kink import inject

from .entity import PhotoStat


@inject(use_factory=True)
class PhotoStatsShower:
    # TODO: Inject PhotoStatRepository
    # TODO: Add Unit Test Case using Mocks(After implementing the repository pattern)

    async def __call__(self) -> PhotoStat:
        return await PhotoStat.avg()
