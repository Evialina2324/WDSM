import math
import matplotlib.pyplot as plt

los=1000
def losowanie():
    global los
    a=16807
    b=0
    c=2147483647
    los=(a*los+b)%c
    return los/c

def poisson(lam):
    X=-1
    S=1
    q=math.exp(-lam)

    while S>q:
        U=losowanie()
        S=S*U
        X+=1

    return X


def normalny(mu, sigma):
    U1=losowanie()
    U2=losowanie()

    Z=math.sqrt(-2*math.log(U1))*math.cos(2*math.pi*U2)

    return mu+sigma*Z

def histogram(dane, tytul):
    plt.hist(dane, bins=30)
    plt.title(tytul)
    plt.show()

N=10000
poisson_dane=[]
for i in range(N):
    poisson_dane.append(poisson(4))

histogram(poisson_dane, "Rozkład Poissona (lambda=4)")

normalne_dane=[]
for i in range(N):
    normalne_dane.append(normalny(0, 1))

histogram(normalne_dane, "Rozkład Normalny (mu=0, sigma=1)")