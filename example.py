import time
from JetCameras import IMX219


if __name__ == "__main__":
    
    camera = IMX219(1, **IMX219.Configs.HD_60FPS)

    while True:

        img = camera.read()
        print(img)
        time.sleep(.1)

