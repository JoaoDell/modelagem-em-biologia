import numpy as np

projs = np.array([10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

freq = np.array([1])

auto = 0.0

fontas = 0.0

pesos = {"projs" : 0.7, "freq" : 0.15, "auto" : 0.1, "fontas" : 0.05}

nf = (pesos["projs"]*np.average(projs) + 
      pesos["freq"]*np.average(freq) + 
      pesos["auto"]*auto + 
      pesos["fontas"]*fontas)

print("NF =", nf) 

