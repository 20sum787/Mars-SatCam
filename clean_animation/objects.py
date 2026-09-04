"""
When a satellit object is instantiated, it needs a name identifier, a colour
and an initial state vector [x,y,z,vx,vy,vz].

After being instantiated, the optimum camera angle is calculated, with the sat
at the centre of the screen
"""

import numpy as np

class SatObj:
    def __init__(self,name,colour,pos,vel):
        self.name = name
        self.pos = pos
        self.vel = vel
        #self.past_pos = np.array([[pos]])
        #self.ground_track = np.array([[]])



