# Import pandas
import pandas as pd

# Import matplotlib
import matplotlib.pyplot as plt

# Load ranked candidates
ranked = pd.read_csv(
    "results/ranked_lhs_candidates.csv"
)

# Select top 10
top10 = ranked.head(10)

# Create figure
plt.figure(
    figsize=(10, 5)
)

# Plot top candidates
plt.bar(
    range(len(top10)),
    top10["EI_score"]
)

plt.xlabel("Top 10 Candidates")
plt.ylabel("EI Score")
plt.title("Top 10 LHS Candidates by EI Score")

plt.savefig(
    "figures/top10_lhs_candidates.png"
)

plt.show()

print()
print("Top 10 LHS candidate figure saved successfully.")