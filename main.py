import cv2
import numpy as np

Xw = np.array([200, 70, 50])
C = np.array([50, 60, -20])

t = (Xw - C).reshape([-1, 1])

R = -C/t

f = 10/0.05
px = 512
py = 512
K = np.array([f, 0, px, 0, f, py, 0, 0, 1]).reshape([3,3])

P = np.dot(K, np.concatenate((R, t), 1))

X = np.append(Xw, 1).reshape([-1, 1])
x = np.dot(P, X).flatten()

Px = int(x[0]/x[2])
Py = int(x[1]/x[2])
print(f"Image Point = x:{Px}, y:{Py}")