import cv2


class IMX219:
    def __init__(
        self,
        camera_id=0,
        capture_size=(3264, 2464),
        output_size=(1024, 768),
        fps=21,
        flip=False,
    ) -> None:

        self._gst_str = IMX219._make_gstreamer_sting(
            camera_id=camera_id,
            capture_width=capture_size[0],
            capture_height=capture_size[1],
            out_width=output_size[0],
            out_height=output_size[1],
            framerate=fps,
            flip_method=2 if flip is True else 0,
        )

        self._gst_cap = cv2.VideoCapture(self._gst_str, cv2.CAP_GSTREAMER)

    def read(self):
        retv, arr = self._gst_cap.read()
        return arr

    @classmethod
    def _make_gstreamer_sting(
        self,
        camera_id=0,
        capture_shape=(3264, 2464),
        resize_to=None,
        framerate=21,
        flip_method=0,
    ):
        # Capture Part
        source_str = f"""
        nvarguscamerasrc sensor_id={camera_id} ! 
        video/x-raw(memory:NVMM),
        width=(int){capture_shape[0]}, height=(int){capture_shape[0]},
        format=(string)NV12, framerate=(fraction){framerate}/1 ! """

        # Convertion Part
        (out_width, out_height) = (
            (resize_to[0], resize_to[1])
            if resize_to is not None
            else (capture_width, capture_height)
        )
        conv_str = f"nvvidconv flip-method={flip_method} ! video/x-raw, width=(int){out_width}, height=(int){out_height}, format=(string)BGRx ! "

        # Sink Part
        sink_str = f"videoconvert ! video/x-raw, format=(string)BGR ! appsink max-buffers=1 drop=true"

        gst_str = ""
        gst_str += source_str
        gst_str += conv_str if resize_to or flip_method else " "
        gst_str += sink_str

        return gst_str

    class Configs:

        # TODO: instead of resizing by default, add resize_to option

        FULL_FRAME = {"capture_size": (3264, 2464), "fps": 21}

        FHD29FPS = {"capture_size": (1920, 1080), "fps": 29}

        HD_30FPS = {"capture_size": (1280, 720), "fps": 30}

        HD_60FPS = {"capture_size": (1280, 720), "fps": 60}


# TODO: decimate

#     class FHD30FPS:


# _1080P_30FPS = {}
# _720P_30FPS = {}
# _720P_60FPS = {}
