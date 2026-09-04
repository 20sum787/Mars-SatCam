
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 1000
dt = 1.999999
t_array = np.arange(0, t_max, dt)

# IMPORTANT - needed so that inital velocity is encoded into solver
x_prev = x - v*dt


# initialise empty lists to record trajectories
x_list = []
v_list = []

# Verlet integration

for t in t_array:
    x_list.append(x)
    a = -k*x/m

    x_old = x

    #x = 2*x - x_prev - (dt**2)*k*x/m
    x = 2*x - x_prev + (dt**2)*a
    x_prev = x_old


'''
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * x / m
    x = x + dt * v
    v = v + dt * a
'''
# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.legend()
plt.show()