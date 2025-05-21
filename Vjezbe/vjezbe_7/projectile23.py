
import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, x0, y0, v0, kut, masa, otpor, dt):
        self.x = x0
        self.y = y0
        self.vx = v0 * np.cos(np.radians(kut))
        self.vy = v0 * np.sin(np.radians(kut))
        self.masa = masa
        self.k = otpor
        self.dt = dt
        self.g = 9.81

        
        self.putanja_x = [self.x]
        self.putanja_y = [self.y]

    def koraci(self):
        ax = -self.k/self.masa * self.vx
        ay = -self.g - self.k/self.masa * self.vy

        
        self.vx += ax * self.dt
        self.vy += ay * self.dt
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt

        self.putanja_x.append(self.x)
        self.putanja_y.append(self.y)

    def euler_simulacija(self):
        while self.y >= 0:
            self.step()
        return self.putanja_x, self.putanja_y
    

    def rk4_simulacija(self):
        x, y = self.x, self.y
        vx, vy = self.vx, self.vy
        traj_x, traj_y = [x], [y]
        dt = self.dt

        while y >= 0:
            # k1
            ax1, ay1 = self.acc(vx, vy)
            k1vx, k1vy = ax1*dt, ay1*dt
            k1x, k1y = vx*dt, vy*dt

            # k2
            ax2, ay2 = self.acc(vx + k1vx/2, vy + k1vy/2)
            k2vx, k2vy = ax2*dt, ay2*dt
            k2x, k2y = (vx + k1vx/2)*dt, (vy + k1vy/2)*dt

            # k3
            ax3, ay3 = self.acc(vx + k2vx/2, vy + k2vy/2)
            k3vx, k3vy = ax3*dt, ay3*dt
            k3x, k3y = (vx + k2vx/2)*dt, (vy + k2vy/2)*dt

            # k4
            ax4, ay4 = self.acc(vx + k3vx, vy + k3vy)
            k4vx, k4vy = ax4*dt, ay4*dt
            k4x, k4y = (vx + k3vx)*dt, (vy + k3vy)*dt

            # Update
            vx += (k1vx + 2*k2vx + 2*k3vx + k4vx)/6
            vy += (k1vy + 2*k2vy + 2*k3vy + k4vy)/6
            x += (k1x + 2*k2x + 2*k3x + k4x)/6
            y += (k1y + 2*k2y + 2*k3y + k4y)/6

            traj_x.append(x)
            traj_y.append(y)
        return traj_x, traj_y



class Projectile:
    def __init__(self, x0, y0, v0, angle, mass, air_resistance, dt):
        self.x = x0
        self.y = y0
        self.vx = v0 * np.cos(np.radians(angle))
        self.vy = v0 * np.sin(np.radians(angle))
        self.mass = mass
        self.k = air_resistance
        self.dt = dt
        self.g = 9.81

    def acc(self, vx, vy):
        ax = -self.k/self.mass * vx
        ay = -self.g - self.k/self.mass * vy
        return ax, ay

    def simulate_euler(self):
        x, y = self.x, self.y
        vx, vy = self.vx, self.vy
        traj_x, traj_y = [x], [y]

        while y >= 0:
            ax, ay = self.acc(vx, vy)
            vx += ax * self.dt
            vy += ay * self.dt
            x += vx * self.dt
            y += vy * self.dt
            traj_x.append(x)
            traj_y.append(y)
        return traj_x, traj_y

    def simulate_rk4(self):
        x, y = self.x, self.y
        vx, vy = self.vx, self.vy
        traj_x, traj_y = [x], [y]
        dt = self.dt

        while y >= 0:
            # k1
            ax1, ay1 = self.acc(vx, vy)
            k1vx, k1vy = ax1*dt, ay1*dt
            k1x, k1y = vx*dt, vy*dt

            # k2
            ax2, ay2 = self.acc(vx + k1vx/2, vy + k1vy/2)
            k2vx, k2vy = ax2*dt, ay2*dt
            k2x, k2y = (vx + k1vx/2)*dt, (vy + k1vy/2)*dt

            # k3
            ax3, ay3 = self.acc(vx + k2vx/2, vy + k2vy/2)
            k3vx, k3vy = ax3*dt, ay3*dt
            k3x, k3y = (vx + k2vx/2)*dt, (vy + k2vy/2)*dt

            # k4
            ax4, ay4 = self.acc(vx + k3vx, vy + k3vy)
            k4vx, k4vy = ax4*dt, ay4*dt
            k4x, k4y = (vx + k3vx)*dt, (vy + k3vy)*dt

            # Update
            vx += (k1vx + 2*k2vx + 2*k3vx + k4vx)/6
            vy += (k1vy + 2*k2vy + 2*k3vy + k4vy)/6
            x += (k1x + 2*k2x + 2*k3x + k4x)/6
            y += (k1y + 2*k2y + 2*k3y + k4y)/6

            traj_x.append(x)
            traj_y.append(y)
        return traj_x, traj_y

if __name__ == "__main__":
    p1 = Projectile(0, 0, 50, 45, 1, 0.1, 0.01)
    x_euler, y_euler = p1.simulate_euler()

    p2 = Projectile(0, 0, 50, 45, 1, 0.1, 0.01)
    x_rk4, y_rk4 = p2.simulate_rk4()

    plt.plot(x_euler, y_euler, label="Euler")
    plt.plot(x_rk4, y_rk4, label="Runge-Kutta 4")
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title('Usporedba putanja (dt=0.01)')
    plt.legend()
    plt.show()




import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, x0, y0, v0, kut, masa, radius, Cd, dt):
        self.x = x0
        self.y = y0
        self.vx = v0 * np.cos(np.radians(angle))
        self.vy = v0 * np.sin(np.radians(angle))
        self.mass = mass
        self.radius = radius
        self.Cd = Cd
        self.dt = dt
        self.g = 9.81
        self.rho = 1.225  # gustoća zraka [kg/m^3]
        self.A = np.pi * radius**2  # površina presjeka [m^2]

    def drag_force(self, vx, vy):
        v = np.sqrt(vx**2 + vy**2)
        Fd = 0.5 * self.Cd * self.rho * self.A * v**2
        # Komponente sile otpora (suprotno smjeru gibanja)
        Fdx = -Fd * (vx / v) if v != 0 else 0
        Fdy = -Fd * (vy / v) if v != 0 else 0
        return Fdx, Fdy

    def acc(self, vx, vy):
        Fdx, Fdy = self.drag_force(vx, vy)
        ax = Fdx / self.mass
        ay = (Fdy - self.mass * self.g) / self.mass
        return ax, ay

    def simulacija_euler(self):
        x, y = self.x, self.y
        vx, vy = self.vx, self.vy
        traj_x, traj_y = [x], [y]

        while y >= 0:
            ax, ay = self.acc(vx, vy)
            vx += ax * self.dt
            vy += ay * self.dt
            x += vx * self.dt
            y += vy * self.dt
            traj_x.append(x)
            traj_y.append(y)
        return traj_x, traj_y

    def simulacija_rk4(self):
        x, y = self.x, self.y
        vx, vy = self.vx, self.vy
        traj_x, traj_y = [x], [y]
        dt = self.dt

        while y >= 0:
            # k1
            ax1, ay1 = self.acc(vx, vy)
            k1vx, k1vy = ax1*dt, ay1*dt
            k1x, k1y = vx*dt, vy*dt

            # k2
            ax2, ay2 = self.acc(vx + k1vx/2, vy + k1vy/2)
            k2vx, k2vy = ax2*dt, ay2*dt
            k2x, k2y = (vx + k1vx/2)*dt, (vy + k1vy/2)*dt

            # k3
            ax3, ay3 = self.acc(vx + k2vx/2, vy + k2vy/2)
            k3vx, k3vy = ax3*dt, ay3*dt
            k3x, k3y = (vx + k2vx/2)*dt, (vy + k2vy/2)*dt

            # k4
            ax4, ay4 = self.acc(vx + k3vx, vy + k3vy)
            k4vx, k4vy = ax4*dt, ay4*dt
            k4x, k4y = (vx + k3vx)*dt, (vy + k3vy)*dt

        
            vx += (k1vx + 2*k2vx + 2*k3vx + k4vx)/6
            vy += (k1vy + 2*k2vy + 2*k3vy + k4vy)/6
            x += (k1x + 2*k2x + 2*k3x + k4x)/6
            y += (k1y + 2*k2y + 2*k3y + k4y)/6

            traj_x.append(x)
            traj_y.append(y)
        return traj_x, traj_y

