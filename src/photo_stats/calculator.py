from uuid import UUID

from kink import inject

from src.photo_stats.rgb_stat_estimator import RgbStatEstimator

from .entity import PhotoStat


@inject(use_factory=True)
class PhotoStatsCalculator:
    # TODO: Listen Event PhotoUploded
    # TODO: Inject PhotoStatRepository
    # TODO: Add Unit Test Case using Mocks(After implementing the repository pattern)
    def __init__(self, rgb_estimator: RgbStatEstimator) -> None:
        self._rgb_estimator = rgb_estimator

    async def __call__(self, asset: bytes, photo_id: UUID) -> PhotoStat:
        rgb_stats = await self._rgb_estimator(asset)
        stat = PhotoStat.calculate(
            photo_id=photo_id,
            red=rgb_stats.red,
            green=rgb_stats.green,
            blue=rgb_stats.blue,
        )
        await stat.save()
        return stat
