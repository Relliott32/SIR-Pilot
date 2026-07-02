import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def derive(I, t, beta, z, eta, mu, muD, v, gamma):
    U = I[0]
    R = I[1]
    C = I[2]
    return [
        (-beta*U)-(eta*U)-(mu*U) -(muD*U)- (z*U) + (gamma), #U
        (beta*U) - (eta*R)-(mu*R) - (muD*R) - (v*R), #R
        (v*R)+(z*U), #C
    ]

#parameter list
beta = .1147 #rate referal into R
z = 1/10 #rate of awareness
mu = 0.005834 # natural death rate
muD = 0.00000239 #death rate related to behavioral issues
eta = 0.0094 #crisis rate
v = 0.009 #rate of connection
gamma = 756 #new cases per day
# total pop in country

N = 2975000 #people with SUDs who are unconnected
#initial conditions
C0 = 562000
R0 = (N-C0)*beta
U0 = N - R0 - C0
times = np.arange(0,50,1) #time in days
sol = odeint(derive, y0=[U0,R0,C0], t=times, args=(beta, z, eta, mu,muD, v, gamma))
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

