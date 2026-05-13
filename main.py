from gurobipy import GRB, Model
from gurobipy import quicksum

model = Model()
model.setParam("TimeLimit", 1800) # Limite de tiempo de 30 minutos

# variables de decision

# 
x = model.addVars(T, vtype = GRB.CONTINUOUS, name = "x")