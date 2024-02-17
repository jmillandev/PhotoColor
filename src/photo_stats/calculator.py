from uuid import UUID

from kink import inject

from .entity import PhotoStat, RgbStat


class RgbStatCalculator:
    async def __call__(self, asset: bytes) -> RgbStat:
        pass


@inject(use_factory=True)
class PhotoStatsCalculator:
    # TODO: Listen Event PhotoUploded
    # TODO: Inject PhotoStatRepository

    async def __call__(self, asset: bytes, photo_id: UUID) -> PhotoStat:
        rgb_stats = await RgbStatCalculator()(asset)
        stat = await PhotoStat.calculate(photo_id=photo_id, rgb_stats=rgb_stats)
        stat.save()
        return stat
