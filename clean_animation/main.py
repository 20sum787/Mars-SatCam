"""
ALL UNITS ARE IN KM

mars avg rad is 3390km
"""

import cv2
import numpy as np
from frame_generator import frame_gen
from physics_engine import sat_update
from objects import SatObj

im_path = r"C:\Users\shrey\OneDrive\Desktop\mars.jpg"
mars_img = cv2.imread(im_path) / 255  # normalise RGB pixels to [0.0, 1.0]
mars_texture_0 = np.asarray(mars_img)

resolution = 512
cv2.namedWindow("MARS SATCAM", cv2.WINDOW_NORMAL)
cv2.resizeWindow("MARS SATCAM", 512,512)

print("Running Demo... Press 'q' in the graphics window to exit.")
# initial position 610km above north pole
init_pos = np.array([0,0,4e6])
init_vel = np.array([2800,2300,0]) # in m/s

sat0 = SatObj(name='MAVEN',colour=np.array([0.0,1.0,0.0]),pos=init_pos,vel=init_vel)

while True:
    # for sat in sat list, update all positions!

    sat_update(sat0)

    sat_pos = sat0.pos
    print("Altitude (km): ",(np.linalg.norm(sat_pos)-3390000)/1000)
    if np.linalg.norm(sat_pos) <= 3500*1000:
        print("Atmosphere collision")
        break
    sat_vel = sat0.vel
    norm_vel = sat_vel / np.linalg.norm(sat_vel)

    camera_pos = sat_pos - sat_vel + sat_pos*0.0005

    rotation_axis = np.linalg.cross(norm_vel,sat_pos)

    frame = frame_gen(sat_pos,camera_pos,rotation_axis,res = resolution,
                      texture = mars_texture_0)

    # convert back to standard 255
    frame = (frame * 255).astype(np.uint8)

    cv2.imshow("MARS SATCAM", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()