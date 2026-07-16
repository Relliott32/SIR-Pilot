import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd
def derive(I, t, beta, z, eta, mu, muD, v, gamma):
    U = I[0]
    R = I[1]
    C = I[2]
    return [
        (-beta*U)-(eta*U)-(mu*U) -(muD*U)- (z*U) + (gamma), #U
        (beta*U) - (eta*R)-(mu*R) - (muD*R) - (v*R) +(z*U), #R
        (v*R), #C
    ]

#parameter list
beta = .1056 #rate referal into R
z = 0.8# rate 0f awareness
mu = 0 # natural death rate
muD = 0#death rate related to behavioral issues
eta = 0 #crisis rate
v = 0.08505378151 #rate of connection
gamma = 00000 #new cases per day
# total pop in country

N = 2975000 #people with SUDs who are unconnected
#initial conditions
C0 = 562000
R0 = (N-C0)*beta
U0 = N - C0-R0
times = np.arange(0,100,1) #time in days
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

# show table of results


df = pd.DataFrame({'Time': times, 'Unaware': U, 'Referred': R, 'Connected': C})
df = df.round(0).astype(int)
print(df)
# show only every 10th timepoint in the table for readability
summary_df = df[df['Time'] % 10 == 0].reset_index(drop=True)
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
table = ax.table(
    cellText=summary_df.values,
    colLabels=summary_df.columns,
    loc='center',
    cellLoc='center',
    colLoc='center',
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.4)
ax.set_title(f'Raw data (every 10th day) - Awareness {z}', pad=20)
fig.tight_layout()
plt.show()
