import time
import sys

sys.path.append("..")

from JetCameras import IMX219, IMX185

if __name__ == "__main__":

    camera = IMX219()

    for i in range(0, 100):

        img = camera.read()
        print(img[0, 0])
        time.sleep(0.01)

    camera.close()
