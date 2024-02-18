from src.photo_stats.rgb_stat_estimator import RgbStatEstimator
from kink import inject
from src.photo_stats.entity import RgbStat
from PIL import Image
from io import BytesIO
from numpy import array, mean, round

@inject(alias=RgbStatEstimator)
class PyllowRgbStatEstimator:
    async def __call__(self, asset: bytes) -> RgbStat:
        image = Image.open(BytesIO(asset))
        matrix = array(image)
        rgb_mean = mean(matrix, axis=(0, 1))
        color_sum = rgb_mean.sum()
        rgb_norm = round(rgb_mean / color_sum * 100)
        # TODO: There is a bug here. The sum of the three colors should be 100 always.
        return RgbStat(
            red=rgb_norm[0],
            green=rgb_norm[1],
            blue=rgb_norm[2]
        )
