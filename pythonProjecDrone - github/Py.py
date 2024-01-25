from djitellopy import Tello
import keyPressModule as kp
import cv2
import time
from threading import Thread
from threading import Event

drone = Tello()
drone.connect()
print(drone.get_battery())

kp.init()


# drone.takeoff()
drone.streamon()

#image in functies global

global img
frame_read = drone.get_frame_read()

keepRecording = True


def getKeyboardInput():

    global videoRec
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 100

    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("d"):
        yv = speed
    elif kp.getKey("a"):
        yv = -speed

    if kp.getKey("l"):
        drone.land()

    if kp.getKey("t"):
        drone.takeoff()

    if kp.getKey("v"):
        videoRec = Event()
        recorder = Thread(target=videoRecorder, args=(videoRec,))
        recorder.start()
        time.sleep(3)

    if kp.getKey("b"):
        videoRec.set()
        global keepRecording
        keepRecording = False

    if kp.getKey("k"):
        cv2.imwrite(f"resources/photo/{time.time()}.png", frame_read.frame)


    return [lr, fb, ud, yv]


def videoRecorder(videoRec):
    height , width, _ = frame_read.frame.shape

    video = cv2.VideoWriter(f"resources/videos/{time.time()}.avi", cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
    while keepRecording:
        time.sleep(1/30)

    video.release()





while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (300, 200))
    cv2.imshow("Image", img)
    kp.main()
    cv2.waitKey(1)
