import cmath
import numpy as np
import matplotlib.pyplot as plt


# k - k value
# T0 - period
# t - time
def ak(k, T0):
    W0 = 2 * cmath.pi / T0

    if k != 0:
        val = (2 / (3 * k * W0)) * cmath.sin(k * W0 * (3 / 4))
    else:
        val = 1 / 2

    return val


# computes Xn
# ak: coefficients
# T: period
# t: Value of Xn at time t
def compute_xn(ak, T, t):

    max_n = len(ak) // 2
    n_list = np.arange(-max_n, max_n + 1, 1)

    f_sum = 0

    for i in range(len(ak)):
        f_sum = f_sum + ak[i] * cmath.exp(2j * (cmath.pi / T) * n_list[i] * t)

    return f_sum


# Graphs a Fourier Series Signal
# ak: coefficients
# T0: period
# t:  vector of times
def graph_xn(ak, T0, t):
    y = [compute_xn(ak, T0, x) for x in t]

    plt.plot(t, y)
    plt.title('Fourier Signal x(t) over Time')
    plt.xlabel('t (seconds)')
    plt.ylabel('x(t)')
    plt.show()


T0 = 3 # period

x = np.arange(-3, 3, 0.01) # interval
N = [3, 5, 11, 32, 100]

n_list = [np.arange(-i, i + 1, 1) for i in N]

coef_list = []
# gets a list of coefficients from n_list
for n in n_list:

    set_list = []

    for k in n:
        set_list.append(ak(k, T0))

    coef_list.append(set_list)

# calculates results
results = []
for i in range(len(N)):

    y = [compute_xn(coef_list[i], T0, t) for t in x]

    results.append(y)

f_color = ['b', 'r', 'g', 'm', '#ffa647', 'k']
# plots combined graph
for i in range(len(results)):
    plt.plot(x, results[i], f_color[i], label=str(N[i]), antialiased=True)

plt.legend(title='N Value')
plt.title('Fourier Signal x(t) over Time')
plt.xlabel('t (seconds)')
plt.ylabel('x(t)')
plt.savefig('Combined.png')
plt.show()

# makes graph for each N
for i in range(len(results)):
    plt.title('Fourier Signal x(t) over Time with N = {}'.format(str(N[i])))
    plt.xlabel('t (seconds)')
    plt.ylabel('x(t)')
    plt.plot(x, results[i], f_color[i], label=str(N[i]), antialiased=True)
    plt.savefig('N-{}'.format(str(N[i])))
    plt.show()

