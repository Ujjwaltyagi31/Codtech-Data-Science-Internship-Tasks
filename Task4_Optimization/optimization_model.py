from pulp import LpMaximize, LpProblem, LpVariable, value

# Define the problem
model = LpProblem(name="profit-maximization", sense=LpMaximize)

# Define decision variables
x = LpVariable(name="Product_A", lowBound=0, cat='Integer')
y = LpVariable(name="Product_B", lowBound=0, cat='Integer')

# Objective function: Maximize 30x + 20y
model += 30 * x + 20 * y, "Total_Profit"

# Constraints
model += 2 * x + 1 * y <= 100, "Machine_1_Hours"
model += 1 * x + 1 * y <= 80, "Machine_2_Hours"

# Solve the problem
model.solve()

# Output the results
print(f"Status: {model.status}, {LpProblem.sense[model.sense]}")
print(f"Produce {x.value()} units of Product A")
print(f"Produce {y.value()} units of Product B")
print(f"Maximum Profit: ₹{value(model.objective)}")
