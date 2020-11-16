import cv2


def gstreamer_pipeline(
    camera_id=0,
    capture_width=3264,
    capture_height=2464,
    display_width=1024,
    display_height=768,
    framerate=10,
    flip_method=0,
):

    return (
        f"nvarguscamerasrc sensor_id=%d ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! "
        "appsink max-buffers=1 drop=true"
        % (
            camera_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


def make_imx219_capture(camera_id):

    gst_string = gstreamer_pipeline(
        camera_id=0,
        capture_width=3264,
        capture_height=2464,
        display_width=1024,
        display_height=768,
        framerate=21,
        flip_method=2,
    )
    cap = cv2.VideoCapture(gst_string, cv2.CAP_GSTREAMER)

    return cap
