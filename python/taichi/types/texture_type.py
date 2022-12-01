from taichi.lang.enums import Format
from taichi.types.primitive_types import f16, f32, i8, i16, i32, u8, u16, u32

FORMAT2TY_CH = {
    Format.r8: (u8, 1),
    Format.r8u: (u8, 1),
    Format.r8i: (i8, 1),
    Format.rg8: (u8, 2),
    Format.rg8u: (u8, 2),
    Format.rg8i: (i8, 2),
    Format.rgba8: (u8, 4),
    Format.rgba8u: (u8, 4),
    Format.rgba8i: (i8, 4),
    Format.r16: (u16, 1),
    Format.r16u: (u16, 1),
    Format.r16i: (i16, 1),
    Format.r16f: (f16, 1),
    Format.rg16: (u16, 2),
    Format.rg16u: (u16, 2),
    Format.rg16i: (i16, 2),
    Format.rg16f: (f16, 2),
    Format.rgb16: (u16, 3),
    Format.rgb16u: (u16, 3),
    Format.rgb16i: (i16, 3),
    Format.rgb16f: (f16, 3),
    Format.rgba16: (u16, 4),
    Format.rgba16u: (u16, 4),
    Format.rgba16i: (i16, 4),
    Format.rgba16f: (f16, 4),
    Format.r32u: (u32, 1),
    Format.r32i: (i32, 1),
    Format.r32f: (f32, 1),
    Format.rg32u: (u32, 2),
    Format.rg32i: (i32, 2),
    Format.rg32f: (f32, 2),
    Format.rgb32u: (u32, 3),
    Format.rgb32i: (i32, 3),
    Format.rgb32f: (f32, 3),
    Format.rgba32u: (u32, 4),
    Format.rgba32i: (i32, 4),
    Format.rgba32f: (f32, 4),
}
import warnings


class TextureType:
    """Type annotation for Textures.

    Args:
        num_dimensions (int): Number of dimensions. For examples for a 2D texture this should be `2`.
    """
    def __init__(self, num_dimensions):
        self.num_dimensions = num_dimensions


class RWTextureType:
    """Type annotation for RW Textures (image load store).

    Args:
        num_dimensions (int): Number of dimensions. For examples for a 2D texture this should be `2`.
        num_channels (int): Number of channels in the texture.
        channel_format (DataType): Data type of texture
        lod (float): Specifies the explicit level-of-detail.
        fmt (ti.Format): Color format of texture
    """
    def __init__(self,
                 num_dimensions,
                 num_channels=None,
                 channel_format=None,
                 lod=0,
                 fmt=None):
        self.num_dimensions = num_dimensions
        if fmt is None:
            warnings.warn(
                "Specifying num_channels and channel_format is deprecated and will be removed in v1.5.0, please specify fmt instead.",
                DeprecationWarning)
            self.num_channels = num_channels
            self.channel_format = channel_format
        else:
            self.num_channels, self.channel_format = FORMAT2TY_CH[fmt]
        self.lod = lod


texture = TextureType
rw_texture = RWTextureType
"""Alias for :class:`~taichi.types.ndarray_type.TextureType`.
"""

__all__ = ['texture', 'rw_texture']
