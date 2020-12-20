import numpy as np

W = np.array([0, 0, 0])
C = np.array([50, 60, -20])
Xw = np.append(np.array([200, 70, 50]), 1).reshape([-1, 1])

t = (W - C).reshape([-1, 1])

R = np.array([[0.6124, -0.3536, 0.7071], [0.7392, 0.5732, 0.35356], [0.2803, 0.7392, 0.624]])

f = 10 / 0.05
px = 512
py = 512
K = np.array([f, 0, px, 0, f, py, 0, 0, 1]).reshape([3, 3])

P = np.dot(K, np.concatenate((R, t), 1))

x = np.dot(P, Xw).flatten()

Px = int(x[0] / x[2])
Py = int(x[1] / x[2])
print(f"Image Point = x:{Px}, y:{Py}")


