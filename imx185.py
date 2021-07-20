from .basecamera import Camera


class IMX185(Camera):
    class MODES:
        FHD29FPS = {"capture_shape": (1920, 1080), "fps": 30}

    def __init__(self, **kwargs):
        super().__init__(**self.MODES.FULL_FRAME, **kwargs)
