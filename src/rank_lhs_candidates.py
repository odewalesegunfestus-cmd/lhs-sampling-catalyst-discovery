# Import pandas
# WHY: Load and rank predicted catalyst results
import pandas as pd

# Load predicted LHS catalysts
# WHY: This file contains prediction and uncertainty for 500 catalysts
predicted = pd.read_csv(
    "results/predicted_lhs_500_catalysts.csv"
)

# Create EI-like score
# WHY: Reward low overpotential and high uncertainty
predicted["EI_score"] = (
    -predicted["Predicted_Overpotential"]
    + predicted["Uncertainty"]
)

# Rank catalysts by EI score
# WHY: Higher EI score means better next catalyst to investigate
ranked = predicted.sort_values(
    by="EI_score",
    ascending=False
)

# Save ranked catalysts
# WHY: Keep best candidate list permanently
ranked.to_csv(
    "results/ranked_lhs_candidates.csv",
    index=False
)

print()
print("TOP 10 LHS CANDIDATES")
print(ranked.head(10))

print()
print("LHS candidates ranked successfully.")