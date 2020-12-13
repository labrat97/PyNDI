import numpy as np
from lib import lib, ffi
from defs import *




class NDISender():
    def __init__(self, name, fourcc=FourCC.BGRA):
        super().__init__() 
        name_cstr = ffi.new("char[]", name.encode())
        self.keepalive = [name_cstr]
        create_config = ffi.new("NDIlib_send_create_t *")
        create_config.p_ndi_name = name_cstr
        create_config.p_groups = ffi.NULL
        create_config.clock_video = True

        self.pNDI_send = lib.NDIlib_send_create(create_config)
        self.name = name
        self.fourcc = fourcc

    def __del__(self):
        lib.NDIlib_send_destroy(self.pNDI_send);
        self.keepalive = []

    # nb. Image should be in uint8 already
    def write(self, image, timecode):
        frame = ffi.new("NDIlib_video_frame_v2_t*")
        frame.xres = image.shape[1]
        frame.yres = image.shape[0]
        frame.FourCC = self.fourcc
        frame.frame_rate_N = 30
        frame.frame_rate_D = 1
        frame.picture_aspect_ratio = 0 # square
        frame.frame_format_type = 1 # progressive
        frame.timecode = ffi.cast('int64_t', timecode)  #  The timecode of this frame in 100ns intervals
        frame.p_data = ffi.cast("uint8_t *", image.ctypes.data)
        frame.line_stride_in_bytes = 4 * frame.xres
        frame.p_metadata = ffi.NULL

        ret = lib.NDIlib_send_send_video_v2(self.pNDI_send, frame);

        # From receiver:    
        #byte_data = np.frombuffer(ffi.buffer(video_frame.p_data, total_bytes))
        #new_data = np.ndarray((height, width, 4), dtype=np.uint8, buffer=byte_data)
        #new_data = new_data.copy() # prevent seg-fault
                
        return True

