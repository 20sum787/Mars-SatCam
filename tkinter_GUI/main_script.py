from layers.layer0 import Application
app = Application()

import numpy as np
#import tkinter as tk
from PIL import Image, ImageTk
from frame_generation import frame_gen
from physics_sim import sat_update
from satobj import SatObj
from gnd_track import gnd_update

im_path = "mars.jpg"
pil_image = Image.open(im_path)
mars_texture_0 = np.asarray(pil_image) / 255.0
# TODO implement gnd track


resolution = 512
height, width = 512, 512

print("Running Demo... Press 'q' in the graphics window to exit.")
# initial position 610km above north pole
init_pos = np.array([0,4.49e6,0])
# should be perpendicular!
init_vel = np.array([2000,0,2090]) # in m/s
global_time = 0
old_gnd = None
sat0 = SatObj(name='MAVEN',colour=np.array([0.0,1.0,0.0]),pos=init_pos,vel=init_vel)

def live_frame():
    global global_time, old_gnd
    # for sat in sat list, update all positions!
    speed_scale = app.contents.bodyframe.sidebar.slider.get()

    dt_new = 0.05*speed_scale

    sat_update(sat0,dt=dt_new)

    sat_pos = sat0.pos
    alt = (np.linalg.norm(sat_pos)-3390000)/1000
    # trivial example to demonstrate different colours
    # in reality, I'll use this for data gaps, etc, to indicate errors
    if alt < 150:
        alt_tag = "error"
    elif alt > 1000:
        alt_tag = "normal"
    else:
        alt_tag = "confirm"
    app.write_to_console(text=f'Altitude: {alt:.2f} km',tag=alt_tag)

    #print("Altitude (km): ",(np.linalg.norm(sat_pos)-3390000)/1000)
    if np.linalg.norm(sat_pos) <= 3500*1000:
        app.write_to_console(text="Atmopshere collision",tag="error")
        return False
    sat_vel = sat0.vel
    norm_vel = sat_vel / np.linalg.norm(sat_vel)

    camera_pos = sat_pos - sat_vel + sat_pos*0.0005

    rotation_axis = np.linalg.cross(norm_vel,sat_pos)

    frame = frame_gen(sat_pos,camera_pos,rotation_axis,res = resolution,
                      texture = mars_texture_0,timestamp=global_time)

    # convert back to standard 255
    frame = (frame * 255).astype(np.uint8)

    if old_gnd is None:

        gnd = gnd_update(sat_pos,pil_image,timestamp = global_time)
    else:
        gnd = gnd_update(sat_pos,pil_image,past_frame = old_gnd,timestamp = global_time)

    old_gnd = gnd

    gnd = (gnd * 255).astype(np.uint8)

    global_time += dt_new

    return frame,gnd


def update_frame():
    # TODO NEED GLOBAL TO STOP GARBAGE COLLECTION
    global tk_image, tk_gnd_img

    # Step A: Get your updated NumPy RGB array (ensure dtype=np.uint8)
    cam_frame,gnd_frame = live_frame()

    # Step B: Convert array to Pillow Image, then to Tkinter PhotoImage
    pil_frame = Image.fromarray(cam_frame)
    tk_image = ImageTk.PhotoImage(image=pil_frame)

    gnd_img = Image.fromarray(gnd_frame)
    tk_gnd_img = ImageTk.PhotoImage(image=gnd_img)

    # Step C: Update the existing Tkinter label with the new frame
    app.contents.bodyframe.cam.label.configure(image=tk_image)
    app.contents.bodyframe.telemetry.gnd.configure(image=tk_gnd_img)

    app.after(50, update_frame)



# 4. Kickstart the loop and the window
update_frame()
app.mainloop()
# TODO label.configure for frame
