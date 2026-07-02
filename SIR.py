
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def derive(I, t, beta, z, eta, mu, v, gamma):
    U = I[0]
    R = I[1]
    C = I[2]
    return [
        (-beta*U)-(eta*U)-(mu*U) - (z*U) + (gamma*U), #U
        (beta*U) - (eta*R)-(mu*R) - (v*R), #R
        (v*C)+(z*U)-(mu*C), #C
    ]

#parameter list
beta = .15 #rate referal into R
z = 1/7 #rate of awarness
mu = 0.05 # natural death rate
muD = 0.18 #death rate related to behavioral issues
eta = 0.01 #crisis rate
v = 1/7 #rate of connection
gamma = .15 #new cases per day
# total pop in country

N = 10000 #total pop (uppercase gamma)
#initial conditions
U0 = 10000000
R0 = 0
C0 = 0
times = np.arange(0,100,1) #time in days
sol = odeint(derive, y0=[U0,R0,C0], t=times, args=(beta, z, eta, mu, v, gamma))
print(sol)
U=sol.T[0]
R=sol.T[1]
C=sol.T[2]

plt.plot(times, U, label='Unaware')
plt.plot(times, R, label='Referred')
plt.plot(times, C, label='Connected')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('URC Model - Behavioural health population')
plt.legend()
plt.show()
