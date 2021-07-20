from .basecamera import Camera

class IMX219(Camera):
    
    class MODES:
        FULL_FRAME = {"capture_shape": (3264, 2464), "fps": 21}
        FHD29FPS = {"capture_shape": (1920, 1080), "fps": 29}
        HD_30FPS = {"capture_shape": (1280, 720), "fps": 30}
        HD_60FPS = {"capture_shape": (1280, 720), "fps": 60}

    def __init__(self):
        super().__init__(**self.MODES.FULL_FRAME)