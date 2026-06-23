
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def derive(I, t, beta, z, N, eta, omega, mu, muD, v, gamma):
    U = I[0]
    A = I[1]
    R = I[2]
    C = I[3]
    return [
        (-beta*U)-(eta*U)-(mu*U)-(muD*U) + gamma*N, #U
        (beta*U) - (z*A)+(omega*C)- (eta*A)-(mu*A)-(muD*A), #A
        (A*z) - (v*R) + (mu*R) - (muD*R), #R
        (eta * U) + (v * R) - (omega *C) -(mu*C) + (eta * A) #C
    ]

#parameter list
beta = .15 #rate of awareness towards programs
z = 1/7 #rate of referral
mu = 0.05 # natural death rate
omega = 0.40 #rate of relapse
muD = 0.30 #death rate related to behavioral issues
eta = 0.05 #rate of people going straight to treatement (S to C)
v = 1/7 #rate of connection
gamma = 0.1 #new cases
# total pop in country

N = 10000 #total pop (uppercase gamma)
#initial conditions
U0 = N
A0 = 0
R0 = 0
C0 = 0
times = np.arange(0,100,1) #time in days
sol = odeint(derive, y0=[U0,A0,R0, C0], t=times, args=(beta, z, N, eta, omega, mu, muD, v, gamma))
print(sol)
U=sol.T[0]
A=sol.T[1]
R=sol.T[2]
C=sol.T[3]

plt.plot(times, U, label='Unaware')
plt.plot(times, A, label='Aware')
plt.plot(times, R, label='Referred')
plt.plot(times, C, label='Connected')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('UARC Model - Behavioural health population')
plt.legend()
plt.show()
