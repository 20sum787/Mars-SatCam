import numpy as np
import math

def frame_gen(target_pos,cam_pos,rot_axis,texture,res=256):
    sat = np.ndarray.astype(target_pos,dtype=np.float32)
    cam = np.ndarray.astype(cam_pos, dtype=np.float32)

    cam_dir = (sat - cam) / np.linalg.norm(sat - cam)
    cam_x = rot_axis / np.linalg.norm(rot_axis)

    cam_up = np.linalg.cross(cam_dir, cam_x)
    cam_y = cam_up / np.linalg.norm(cam_up)

    #

    x = np.linspace(-1, 1, res)
    y = np.linspace(-1, 1, res)
    xgrid, ygrid = np.meshgrid(x, y)
    focal_length = 2

    h, w = xgrid.shape
    # reshaping needed to make multiplication compatible
    x3d = np.reshape(xgrid, (h, w, 1))
    y3d = np.reshape(ygrid, (h, w, 1))
    ray_dirs = x3d * cam_x + y3d * cam_y + focal_length * cam_dir

    ray_mags = np.linalg.norm(ray_dirs, axis=-1, keepdims=True)
    ray_dirs = ray_dirs / ray_mags

    # checking for intersection

    rad = 3390*1000
    b = 2 * np.sum(ray_dirs * cam, axis=-1)
    c = np.sum(cam * cam) - rad ** 2

    discrim = b ** 2 - 4 * c
    canvas = np.zeros((res, res, 3))

    hit_mask_planet = discrim > 0
    # creates a mask array of TRUE/FALSE for pixel hits
    # TODO overrwrite hit mask for satellites/asteroids

    if np.any(hit_mask_planet):
        # only - value, as the lowest value of t is the one that is hit first

        hit_ts = (-b[hit_mask_planet] - np.sqrt(discrim[hit_mask_planet])) / 2
        hit_pts = cam + hit_ts[:, np.newaxis] * ray_dirs[hit_mask_planet]

        # next, for each hit point, we map to lat/long on the rectangular image

        norm_hits = hit_pts / rad
        norm_hits = np.clip(norm_hits, -1.0, 1.0)

        phi = np.asin(norm_hits[:, 2])
        theta = np.atan2(norm_hits[:, 1], norm_hits[:, 0])

        # Map angles mathematically to a [0.0, 1.0] image grid range
        u = (theta + math.pi) / (2.0 * math.pi)
        v = (phi + (math.pi / 2.0)) / math.pi
        # Invert v so north pole is at the top of the texture file
        v = 1.0 - v

        # Convert [0, 1] percentages to real pixel indexes of your loaded Mars image
        tex_h, tex_w, _ = texture.shape
        tex_x = (u * (tex_w - 1)).astype(int)
        tex_y = (v * (tex_h - 1)).astype(int)

        # Vectorized texture mapping: instantly map the pixels onto the sphere shape
        canvas[hit_mask_planet] = texture[tex_y, tex_x]

    # 4. Project 3D Lander onto the 2D Viewscreen

    screen_x = int(res / 2)
    screen_y = int(res / 2)
    # TODO CUSTOM COLOUR
    canvas[screen_y - 1:screen_y + 2, screen_x - 1:screen_x + 2] = (
        np.array([0.0, 1.0, 1.0]))
    # BGR??
    return canvas



