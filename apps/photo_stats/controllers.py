from src.photo_stats.entity import RgbStat
from src.photo_stats.shower import PhotoStatsShower


async def show() -> RgbStat:
    shower = PhotoStatsShower()
    photo_stat = await shower()
    return photo_stat
