from src.shared.domain.exceptions.base import UNKNOWN, DomainException

class CantUploadEmptyAsset(DomainException):
    def __init__(self):
        super().__init__(400, "Asset can't be empty", 'asset')


class UnsupportedAssetMediaType(DomainException):
    def __init__(self):
        super().__init__(415, "Currently just 'image/jpeg' is supported as Asset", 'asset')
