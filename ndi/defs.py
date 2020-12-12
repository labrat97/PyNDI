class FrameType(enum.IntEnum):
    type_none = 0
    type_video = 1
    type_audio = 2
    type_metadata = 3
    type_error = 4

    # emitted when the type has changed
    type_status_change = 100 

class ColorFormat(enum.IntEnum):
    format_BGRX_BGRA = 0 # No alpha channel: BGRX, Alpha channel: BGRA
    format_UYVY_BGRA = 1 # No alpha channel: UYVY, Alpha channel: BGRA
    format_RGBX_RGBA = 2 # No alpha channel: RGBX, Alpha channel: RGBA
    format_UYVY_RGBA = 3 # No alpha channel: UYVY, Alpha channel: RGBA
