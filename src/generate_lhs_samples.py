# Import pandas
# WHY: Create and save catalyst table
import pandas as pd

# Import Latin Hypercube sampler
# WHY: Generate well-spread virtual catalyst samples
from scipy.stats import qmc

# Create LHS sampler
# WHY: We now generate 5 catalyst features
sampler = qmc.LatinHypercube(
    d=5,
    seed=42
)

# Generate 500 samples
samples = sampler.random(
    n=500
)

# Convert samples into real catalyst ranges
lhs_catalysts = pd.DataFrame()

lhs_catalysts["Ni_fraction"] = samples[:, 0]
lhs_catalysts["Co_fraction"] = samples[:, 1]
lhs_catalysts["Fe_fraction"] = samples[:, 2]

# Calculate total metal fraction
# WHY: Ni + Co + Fe must equal 1
total_metal = (
    lhs_catalysts["Ni_fraction"]
    + lhs_catalysts["Co_fraction"]
    + lhs_catalysts["Fe_fraction"]
)

# Normalize metal fractions
# WHY: Convert raw LHS values into valid catalyst composition fractions
lhs_catalysts["Ni_fraction"] = lhs_catalysts["Ni_fraction"] / total_metal
lhs_catalysts["Co_fraction"] = lhs_catalysts["Co_fraction"] / total_metal
lhs_catalysts["Fe_fraction"] = lhs_catalysts["Fe_fraction"] / total_metal

# Add calcination temperature
# WHY: Convert LHS values into realistic temperature range
lhs_catalysts["Calcination_temp_C"] = (
    300 + samples[:, 3] * (700 - 300)
)

# Add surface area
# WHY: Convert LHS values into realistic surface area range
lhs_catalysts["Surface_area_m2g"] = (
    50 + samples[:, 4] * (200 - 50)
)

# Check metal fraction sum
# WHY: Confirm Ni + Co + Fe equals 1
lhs_catalysts["Metal_sum"] = (
    lhs_catalysts["Ni_fraction"]
    + lhs_catalysts["Co_fraction"]
    + lhs_catalysts["Fe_fraction"]
)

# Save LHS catalysts
# WHY: Keep realistic LHS search space permanently
lhs_catalysts.to_csv(
    "results/lhs_500_realistic_catalysts.csv",
    index=False
)

print()
print("METAL FRACTION CHECK")
print(lhs_catalysts["Metal_sum"].head())

print()
print("FIRST 10 REALISTIC LHS CATALYSTS")
print(lhs_catalysts.head(10))

print()
print("TOTAL LHS CATALYSTS")
print(len(lhs_catalysts))

print()
print("Realistic LHS catalysts saved successfully.")