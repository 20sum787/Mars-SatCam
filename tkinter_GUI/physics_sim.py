import numpy as np
# TODO investigate symplectic
# physics engine deals with satellite position
#from objects import SatObj
G = 6.67e-11
M = 6.42e23

def sat_update(sat_obj,dt=0.05):
    pos_mag = np.linalg.norm(sat_obj.pos)
    unit_pos = sat_obj.pos / pos_mag
    accel = (-G * M / (pos_mag ** 2)) * unit_pos

    sat_obj.vel = sat_obj.vel + dt*accel
    sat_obj.pos = sat_obj.pos + dt*sat_obj.vel

    # TODO add historical trajectory, and map out ground track, return all

    return True
    # updates the satellite object