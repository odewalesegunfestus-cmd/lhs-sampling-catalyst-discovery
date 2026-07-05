# Import pandas
import pandas as pd

# Import matplotlib
import matplotlib.pyplot as plt

# Create grid search points
grid_points = []

for ni in range(5, 96, 5):

    co = 100 - ni

    grid_points.append(
        [
            ni / 100,
            co / 100
        ]
    )

grid = pd.DataFrame(
    grid_points,
    columns=[
        "Ni_fraction",
        "Co_fraction"
    ]
)

# Load LHS points
lhs = pd.read_csv(
    "results/lhs_catalysts.csv"
)

# Plot grid search
plt.figure(figsize=(6, 6))

plt.scatter(
    grid["Ni_fraction"],
    grid["Co_fraction"],
    label="Grid Search"
)

plt.scatter(
    lhs["Ni_fraction"],
    lhs["Co_fraction"],
    label="LHS"
)

plt.xlabel("Ni_fraction")
plt.ylabel("Co_fraction")
plt.title("Grid Search vs LHS Sampling")
plt.legend()

plt.savefig(
    "figures/grid_vs_lhs.png"
)

plt.show()

print()
print("Grid vs LHS comparison saved successfully.")