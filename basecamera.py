import cv2


class Camera:
    def __init__(
        self,
        camera_id=0,
        capture_shape=(3264, 2464),
        resize_to=(1024, 768),
        fps=21,
        flip=False,
    ) -> None:

        # Capture Part
        source_str = f"""
        nvarguscamerasrc sensor_id={camera_id} ! 
        video/x-raw(memory:NVMM),
        width=(int){capture_shape[0]}, height=(int){capture_shape[1]},
        format=(string)NV12, framerate=(fraction){fps}/1 ! """

        # Convertion Part
        if resize_to is not None:
            (out_width, out_height) = (resize_to[0], resize_to[1])
        else:
            (out_width, out_height) = (capture_shape[0], capture_shape[1])

        conv_str = f"nvvidconv flip-method={2 if flip is True else 0} ! video/x-raw, width=(int){out_width}, height=(int){out_height}, format=(string)BGRx ! "

        # Sink Part
        sink_str = f"videoconvert ! video/x-raw, format=(string)BGR ! appsink max-buffers=1 drop=true"

        gst_str = ""
        gst_str += source_str
        gst_str += conv_str if (resize_to or flip) else " "
        gst_str += sink_str

        self._gst_cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

    def read(self):
        retv, arr = self._gst_cap.read()
        return arr

    def close(self):
        self._gst_cap.release()
