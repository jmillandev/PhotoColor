from Pylette import Palette
from PIL import Image
from io import BytesIO
from numpy import asarray
from kink import inject
from src.color_palettes.palette_extractor import ColorPaletteExtractor
from src.color_palettes.entity import Colors
from Pylette.src.color_extraction import k_means_extraction
from typing import Tuple

@inject(alias=ColorPaletteExtractor)
class PyletteColorPaletteExtractor:
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
            self._tuple_int_to_hex(palette[4].rgb)
        )

    def _tuple_int_to_hex(self, color: Tuple[int, int, int]) -> str:
        return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
