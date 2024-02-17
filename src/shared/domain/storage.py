from typing import Protocol, runtime_checkable


@runtime_checkable
class AssetStorage(Protocol):
    async def save(self, asset: bytes, path: str) -> None:
        ...
