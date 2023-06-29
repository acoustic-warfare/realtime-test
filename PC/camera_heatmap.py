# importing the libraries
import cv2
import numpy as np
import random
from play import play_sound
from multiprocessing import Process

light_blue = [27, 170, 222]
blue = [66, 106, 253]
dark_blue = [60, 40, 170]
yellow = [250, 250, 20]
orange = [244, 185, 60]
green = [100, 200, 100]
colors = [light_blue, blue, dark_blue, yellow, orange, green]

shape = (30, 32, 3)
small_heatmap = np.zeros(shape, dtype=np.uint8)

# Very unoptimized. Use numpy functionalities for writing the pixels
def simulate_heatmap():
    for i in range(30):
        for j in range(32):
            #Generate random colors
            index = random.randint(0, 5)
            small_heatmap[i][j] = colors[index]
    
    heatmap = cv2.resize(small_heatmap, (1280, 720))
    return heatmap

def display_camera():
    # Setup camera
    cap = cv2.VideoCapture(0)

    # Read heatmap and resize
#    print("IMPORTANT: YOU NEED PHOTO PERMISSION IF YOU ARE AT A SECURE/VITAL INSTALLATION!!!")
 #   if input("Do you have a valid photo permission? (Y/n)") == "Y":
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Add heatmap to current frame
        heatmap = simulate_heatmap()
        dst = cv2.addWeighted(frame, 0.6, heatmap, 0.4, 0)
        cv2.imshow('WebCam', dst)
        if cv2.waitKey(1) == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def display_camera_and_sound():
    sound = Process(target=play_sound)
    display = Process(target=display_camera)
    display.start()
    sound.start()
    display.join()
    sound.join()    
#display_camera()

display_camera_and_sound()