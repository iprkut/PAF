
import matplotlib.pyplot as plt


q_elektron = -1.602e-19   #C
m_elektron = 9.109e-31    #kg
q_pozitron = 1.602e-19    #C
m_pozitron = 9.109e-31    #kg


x0, y0, z0 = 0, 0, 0       #m
vx0, vy0, vz0 = 1, 1, 1    # m/s


Ex, Ey, Ez = 0.2, 0, 0           #V/m
Bx, By, Bz = 0, 0, 1             #T

dt = 0.01   #s
N = 2000      # broj koraka

def simulacija(q, m):
    x, y, z = x0, y0, z0
    vx, vy, vz = vx0, vy0, vz0
    X, Y, Z = [x], [y], [z]

    for i in range(N):
        ax = (q/m) * (Ex + vy*Bz - vz*By)
        ay = (q/m) * (Ey + vz*Bx - vx*Bz)
        az = (q/m) * (Ez + vx*By - vy*Bx)

        
        vx += ax*dt
        vy += ay*dt
        vz += az*dt

        
        x += vx*dt
        y += vy*dt
        z += vz*dt

        
        X.append(x)
        Y.append(y)
        Z.append(z)
    return X, Y, Z


X_e, Y_e, Z_e = simulacija(q_elektron, m_elektron)
X_p, Y_p, Z_p = simulacija(q_pozitron, m_pozitron)


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(X_e, Y_e, Z_e, label="Elektron", c='blue')
ax.plot(X_p, Y_p, Z_p, label="Pozitron", c='red')
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("z (m)")

plt.title("Putanja elektrona i pozitrona u električnom i magnetskom polju")
plt.legend()
plt.show()