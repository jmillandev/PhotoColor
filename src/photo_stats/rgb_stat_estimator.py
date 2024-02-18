from typing import Protocol, runtime_checkable

from .entity import RgbStat


@runtime_checkable
class RgbStatEstimator(Protocol):
    async def __call__(self, asset: bytes) -> RgbStat:
        ...
