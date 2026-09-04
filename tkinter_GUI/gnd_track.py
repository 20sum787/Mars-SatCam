import numpy as np
import math

def gnd_update(target_pos,equirect):
    # TODO simpler - resize first!
    can_w = 520
    can_h = 260
    resized_map = equirect.resize((can_w,can_h),5)
    canvas = np.array(resized_map) / 255.0

    sat = np.ndarray.astype(target_pos,dtype=np.float32)
    surface_pt = sat/np.linalg.norm(sat)

    phi = np.asin(surface_pt[1])
    theta = np.atan2(surface_pt[2], surface_pt[0])

    # Map angles mathematically to a [0.0, 1.0] image grid range
    u = (theta + math.pi) / (2.0 * math.pi)
    v = (phi + (math.pi / 2.0)) / math.pi
    # Invert v so north pole is at the top of the texture file
    v = 1.0 - v

    # Convert [0, 1] percentages to real pixel indexes of your loaded Mars image

    #sat_x = (u * (can_w - 1)).astype(int)
    #sat_y = (v * (can_h - 1)).astype(int)

    sat_x = int(np.round(u * (can_w - 1)))
    sat_y = int(np.round(v * (can_h - 1)))

    y_min = max(0, sat_y - 2)
    y_max = min(can_h, sat_y + 2)
    x_min = max(0, sat_x - 2)
    x_max = min(can_w, sat_x + 2)

    # Draws a cyan square marker [0.0, 1.0, 1.0] over the map
    canvas[y_min:y_max, x_min:x_max] = np.array([0.0, 1.0, 0.0])

    #canvas[sat_x-2:sat_x+2,sat_y-2:sat_y+2] = np.array([0.0, 1.0, 1.0])

    return canvas

