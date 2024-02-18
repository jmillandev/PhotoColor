from kink import inject

from .entity import PhotoStat, RgbStat


@inject(use_factory=True)
class PhotoStatsShower:
    # TODO: Inject PhotoStatRepository
    # TODO: Add Unit Test Case using Mocks(After implementing the repository pattern)

    async def __call__(self) -> RgbStat:
        return await PhotoStat.avg()  # type: ignore[misc, call-arg]
