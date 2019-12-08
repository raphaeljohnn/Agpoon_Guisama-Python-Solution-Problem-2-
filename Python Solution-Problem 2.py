import numpy as np

x1, y1, x2, y2, x3, y3 = map(int, input("Enter the (x,y) points consecutively: ").split())

X = np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])
Y = np.negative(np.sum(np.power(X[:, :-1], 2), axis=1))
Y = np.transpose(Y)
Z = np.linalg.inv(X).dot(Y)

h = -Z[0]/2 # X-coordinate of the center
k = -Z[1]/2 # Y-coordinate of the center
radius = np.sqrt((x1-h)**2 + (y1-k)**2) # Use any point then compute for the distance from the center.

print('Center: ', h, k)
print('Radius ', radius)
print('[D E F] = ', Z)
