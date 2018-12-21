from gurobipy import *

m = Model('test')

x = m.addVar(lb = -2, ub = 3, vtype = 'C')

m.setObjective(x, GRB.MAXIMIZE)

m.optimize()

print(m.getObjective().getValue())
