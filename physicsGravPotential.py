from matplotlib import pyplot as plt
from tqdm import tqdm

G = 6.67*10**-11
m1 = 1000
m2 = 2
r_init = 100000

x = []
y = []

def gravPotential(m1, m2, r):
    numerator = G*m1*m2
    return -numerator/r

while r_init>20:
    r_final = r_init-10 
    r_difference = r_final-r_init
    y.append(gravPotential(m1, m2, r_final)-gravPotential(m1, m2, r_init))
    x.append(r_init)

    
    r_init-=10

plt.plot(x, y)
plt.title("Difference in Gravitational Potential (final-initial) for difference in radius", fontsize='small')
plt.xlabel("Radius, r/m")
plt.ylabel("Gravitational Potential, V")

plt.show()
    
