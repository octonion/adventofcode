import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

orbits = []
bodies = set({})
for line in sys.stdin:
    orbit = line.strip()
    orbits += [orbit]
    bodies = bodies.union(set(orbit.split(")")))

n = len(bodies)
m = np.zeros((n,n))

bodies = list(bodies)
for orbit in orbits:
    edge = orbit.split(")")
    left = bodies.index(edge[0])
    right = bodies.index(edge[1])
    m[left,right] = 1

m = floyd_warshall(m,directed=True,overwrite=True,unweighted=True)
i = bodies.index("COM")
print(int(round(sum(m[i]))))
