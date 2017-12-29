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


v1 = vec1 + vec2
print("v1:", v1)
vec1 += vec2
print("vec1:", vec1)
print("vec2", vec2)
v3 = vec2 * 2
print("v3:", v3)
v4 = vec4 + 3
print("v4:", v4)
v5 = np.sin(vec5)
print("v5:", v5)
lst = v5.tolist()
print(lst)
