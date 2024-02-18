from io import BytesIO
from typing import Tuple

from kink import inject
from numpy import asarray
from PIL import Image
from Pylette import Palette  # type: ignore[import-untyped]
from Pylette.src.color_extraction import (  # type: ignore[import-untyped]
    k_means_extraction,
)

from src.color_palettes.entity import Colors
from src.color_palettes.palette_extractor import ColorPaletteExtractor


@inject(alias=ColorPaletteExtractor)
class PyletteColorPaletteExtractor:
    # TODO: Add Test case
    async def __call__(self, asset: bytes) -> Colors:
        image = Image.open(BytesIO(asset)).resize((256, 256))
        width, height = image.size
        arr = asarray(image)
        palette_size = 5
        colors = k_means_extraction(arr, height, width, palette_size)
        colors.sort(reverse=True)
        palette = Palette(colors)
        return Colors(
            self._tuple_int_to_hex(palette[0].rgb),
            self._tuple_int_to_hex(palette[1].rgb),
            self._tuple_int_to_hex(palette[2].rgb),
            self._tuple_int_to_hex(palette[3].rgb),
            self._tuple_int_to_hex(palette[4].rgb),
        )

    def _tuple_int_to_hex(self, color: Tuple[int, int, int]) -> str:
        return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
