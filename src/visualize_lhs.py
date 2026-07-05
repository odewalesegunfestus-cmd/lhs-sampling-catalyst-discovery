# Import pandas
import pandas as pd

# Import matplotlib
import matplotlib.pyplot as plt

# Load LHS catalysts
lhs = pd.read_csv(
    "results/lhs_catalysts.csv"
)

# Create scatter plot
plt.figure(
    figsize=(6, 6)
)

plt.scatter(
    lhs["Ni_fraction"],
    lhs["Co_fraction"]
)

plt.xlabel("Ni_fraction")
plt.ylabel("Co_fraction")

plt.title(
    "LHS Sampling Distribution"
)

plt.savefig(
    "figures/lhs_distribution.png"
)

plt.show()

print()
print("LHS visualization saved successfully.")