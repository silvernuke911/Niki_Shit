import numpy as np 
import matplotlib.pyplot as plt

def randomizer(n, average, stddev):
    samples = np.random.normal(loc=average, scale=stddev, size=n)
    return samples

def RTDH():
    n        = 6
    mean_d   = 25.33333333
    stddev_d = 11.11305539
    mean_v   = 29.72669069
    stddev_v = 10.16242939

    distances = randomizer(n,mean_d,stddev_d)
    vels      = randomizer(n,mean_v,stddev_v)
    times = distances/vels
    for dis in distances:
        print(round(dis))
    print()
    for t in times:
        print(round(t,2))

N=25
def randomizer(n, average, stddev):
    samples = np.random.normal(loc=average, scale=stddev, size=n)
    return samples

mean_ets, stdev_ets = 0,0
mean_eit, stdev_eit = 0,0
mean_epl, stdev_epl = 0,0
mean_nts, stdev_nts = 0,0
mean_nit, stdev_nit = 0,0
mean_npl, stdev_npl = 0,0
ets = randomizer(N,mean_ets,stdev_ets)
eit = randomizer(N,mean_eit,stdev_eit)
epl = randomizer(N,mean_epl,stdev_epl)
nts = randomizer(N,mean_nts,stdev_nts)
nit = randomizer(N,mean_nit,stdev_nit)
npl = randomizer(N,mean_npl,stdev_npl)

codes = ['C','P','N','S']
for code in codes :
    for i in range(1,6):
        for j in range(1,6):
            print(f'{code}{i}W6,{code}W6,{j},')