import numpy as np

W = np.array([0, 0, 0])  # World cordinate origin
C = np.array([50, 60, -20])  # Camera cordinate origin in world coordinate
Xw = np.array([200, 70, 50])  # 3D image point in world coordinate

# Calculate Intrinsic Params
f = 10 / 0.05
px = 512
py = 512
K = np.array([f, 0, px, 0, f, py, 0, 0, 1]).reshape([3, 3])

# Calculate Extrinsic Params

R = np.array([[0.6124, -0.3536, 0.7071], [0.7392, 0.5732, 0.35356], [0.2803, 0.7392, 0.624]])
T = (W - C).reshape([-1, 1])
t = -np.dot(R, T)
Rt = np.concatenate((R, t), 1)
IT = np.concatenate((np.identity(3), -T), 1)

# Translate First
P = np.dot(K, R)
P = np.dot(P, IT)

# Rotate First
P = np.dot(K, Rt)

# Convert world coordinate to image point
X = np.append(Xw, 1).reshape([-1, 1])
x = np.dot(P, X).flatten()
Px = int(x[0] / x[2])
Py = int(x[1] / x[2])
print(f"Cartesian Image Point: x={Px}, y={Py}")
