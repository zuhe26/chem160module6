from ising_class import *
Temp=.5
n=20
ntrials=500000
nequil=100000

ising1=ising(Temp, n)
ising1.randomize()

ising1.trials(nequil)
ising1.resetprops()
while Temp<4.:
    ising1.changeTemp(Temp)
    ising1.trials(nequil)
    ising1.resetprops()
    for i in range(ntrials):
        ising1.trial()
        ising1.addprops()
    ising1.calcprops()
    Temp+=.2
ising1.printsys()
