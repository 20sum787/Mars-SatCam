import cv2
import numpy as np
import math

im_path = r"C:\Users\shrey\OneDrive\Desktop\mars.jpg"
mars_img = cv2.imread(im_path) / 255.0  # Normalize to [0.0, 1.0]
mars_texture_0 = np.asarray(mars_img)

def live_frame(sat_pos, cam_pos, circle_pin, texture, res=128):
    sat = np.ndarray.astype(sat_pos, dtype=np.float32)
    cam = np.ndarray.astype(cam_pos, dtype=np.float32)

    cam_dir = (sat - cam) / np.linalg.norm(sat - cam)

    cam_up = np.linalg.cross(cam_dir,circle_pin)
    cam_y = cam_up / np.linalg.norm(cam_up)
    # x is the same as circle pin!
    x_raw = np.linalg.cross(cam_y,cam_dir)
    cam_x = x_raw / np.linalg.norm(x_raw)

    x = np.linspace(-1, 1, res)
    y = np.linspace(-1, 1, res)
    xgrid, ygrid = np.meshgrid(x, y)
    focal_length = 2

    h, w = xgrid.shape

    # Reshape to explicitly add the trailing 1 dimension
    x3d = np.reshape(xgrid, (h, w, 1))
    y3d = np.reshape(ygrid, (h, w, 1))
    # TODO add focal length instead of subtract?
    ray_dirs = x3d * cam_x + y3d * cam_y + focal_length * cam_dir

    # Calculates the norm for each individual 3D pixel vector
    ray_norms = np.linalg.norm(ray_dirs, axis=-1, keepdims=True)
    ray_dirs = ray_dirs / ray_norms

    # ray_startpts = np.full((h,w),cam)
    # ray_startpts = np.broadcast_to(cam, (h, w, 3))

    # checking for intersection

    rad = 3
    b = 2 * np.sum(ray_dirs * cam, axis=-1)
    c = np.sum(cam * cam) - rad ** 2

    discrim = b ** 2 - 4 * c
    canvas = np.zeros((res, res, 3))

    hit_mask_planet = discrim > 0
    # TODO then overrite this hit mask with that for asteroids!

    if np.any(hit_mask_planet):
        # only - value, as the lowest value of t is the one that is hit first

        hit_ts = (-b[hit_mask_planet] - np.sqrt(discrim[hit_mask_planet])) / 2
        hit_pts = cam + hit_ts[:, np.newaxis] * ray_dirs[hit_mask_planet]

        # next, for each hit point, we map to lat/long on the rectangular image

        norm_hits = hit_pts / rad
        norm_hits = np.clip(norm_hits, -1.0, 1.0)

        phi = np.asin(norm_hits[:, 1])
        theta = np.atan2(norm_hits[:, 2], norm_hits[:, 0])

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

    canvas[screen_y - 1:screen_y + 2, screen_x - 1:screen_x + 2] = (
        np.array([0.0, 1.0, 1.0]))
        # BGR??
    return canvas


# ──── LIVE LOOP DEMO ────
if __name__ == "__main__":
    resolution = 256
    cv2.namedWindow("Live Matrix Camera Simulation", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live Matrix Camera Simulation", 512,
                     512)  # Upscale window for display

    time_step = 0

    print("Running Demo... Press 'q' in the graphics window to exit.")

    old_pos = [0.0, 0.0, 4.0]

    while True:
        time_step += 0.001
        # --- DUMMY KINEMATICS LOOP ---
        # Substitute this entire block with your Verlet or Euler-SI script outputs
        # Simulated lander orbiting Mars elliptically

        lander_x = 5.0*math.sin(time_step)
        lander_y = 0.0
        lander_z = 5.0 * math.cos(time_step)
        lander_pos = np.array([lander_x, lander_y, lander_z])

        # 2. CHASE GEOMETRY: Get the direction vector the satellite is moving
        vel = lander_pos - old_pos
        vel = vel / np.linalg.norm(vel)

        camera_pos = lander_pos - vel*0.001 + lander_pos*0.0002

        pin_centre = np.linalg.cross(vel,lander_pos)

        # --- EXECUTE PYTORCH RENDER ---
        frame = live_frame(lander_pos, camera_pos, pin_centre,
                           res=resolution, texture=mars_texture_0)

        # Convert PyTorch float tensor [0.0, 1.0] back to standard uint8 NumPy image matrix
        frame = (frame * 255).astype(np.uint8)

        # Render to Screen Window
        cv2.imshow("Live Matrix Camera Simulation", frame)

        old_pos = lander_pos

        # Handle manual user breaks
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()