import cv2

def gstreamer_pipeline(
    camera_id=0,
    capture_width=3264,
    capture_height=2464,
    out_width=1024,
    out_height=768,
    framerate=10,
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



def make_imx219_capture(camera_id):

    gst_string = gstreamer_pipeline(
        camera_id=camera_id,
        framerate=21,
        flip_method=2,
    )

    cap = cv2.VideoCapture(gst_string, cv2.CAP_GSTREAMER)

    return cap
