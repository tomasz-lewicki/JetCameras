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
        capture_width=3264,
        capture_height=2464,
        out_width=1024,
        out_height=768,
        framerate=21,
        flip_method=0,
    ):

        gst_string = f"""
        nvarguscamerasrc sensor_id={camera_id} ! 
        video/x-raw(memory:NVMM),
        width=(int){capture_width}, height=(int){capture_height},
        format=(string)NV12, framerate=(fraction){framerate}/1 !
        nvvidconv flip-method={flip_method} !
        video/x-raw, width=(int){out_width}, height=(int){out_height}, format=(string)BGRx !
        videoconvert !
        video/x-raw, format=(string)BGR !
        appsink max-buffers=1 drop=true
        """

        return gst_string
    
    class Configs:

        FHD29FPS={
            'capture_size': (1920, 1080),
            'output_size': (1920, 1080),
            'fps': 29
            }
        
        HD_30FPS={
            'capture_size': (1280, 720),
            'output_size': (1280, 720),
            'fps': 30
            }
        
        HD_60FPS={
            'capture_size': (1280, 720),
            'output_size': (1280, 720),
            'fps': 60
            }

        

# TODO: decimate

#     class FHD30FPS:




# _1080P_30FPS = {}
# _720P_30FPS = {}
# _720P_60FPS = {}
