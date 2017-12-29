import numpy as np

vec1 = np.array([0., 1., 2., 3., 4.])
vec2 = np.arange(0, 5, 1, dtype=float)
vec3 = np.linspace(0, 4, 5)
vec4 = np.zeros(5)
for i in range(5):
    vec4[i] = i
vec5 = np.loadtxt("data.txt")
print("vec1:", vec1)
print("vec2:", vec2)
print("vec3:", vec3)
print("vec4:", vec4)
print("vec5:", vec5)