import numpy as np
import matplotlib.pyplot as plt

G = 6.67e-11
M = 6.42e23
r_km = 10000
#v_mag0 = np.sqrt(G*M/r_km/1000)
v_mag0 = 2000
print(v_mag0)

r = np.array([0,0,r_km*1000])
perp_circle = np.array([0,1,0])

v_raw = np.linalg.cross(r,perp_circle)
v = v_mag0*(v_raw/np.linalg.norm(v_raw))
#v = np.array([0,0,0])

t_max = 30000
dt = 0.1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
r_list = []
v_list = []

for t in t_array:


    r_mag = np.linalg.norm(r)
    v_mag = np.linalg.norm(v)
    r_list.append(r_mag/1000)
    v_list.append(v_mag)


    if r_mag > 0:
        r_normal = r / r_mag
    else:
        r_normal = r


    a = (-G*M/(r_mag**2))*r_normal


    r = r + dt*v

    v = v + dt*a

r_array = np.array(r_list)
v_array = np.array(v_list)
# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, r_array, label='r (km)')
#plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()