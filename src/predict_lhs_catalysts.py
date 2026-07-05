# Import pandas
import pandas as pd

# Load LHS catalysts
lhs_catalysts = pd.read_csv(
    "results/lhs_500_realistic_catalysts.csv"
)

print()
print("LHS CATALYSTS LOADED")
print(lhs_catalysts.head())

print()
print("TOTAL LHS CATALYSTS")
print(len(lhs_catalysts))

# Load training catalyst dataset
training_data = pd.read_csv(
    "data/catalyst_data.csv"
)

# Define training features
X = training_data[
    [
        "Ni_fraction",
        "Co_fraction",
        "Fe_fraction"
    ]
]

# Define target
y = training_data[
    "Overpotential_mV"
]

print()
print("TRAINING DATA LOADED")
print(X.head())

# Import GPR
from sklearn.gaussian_process import GaussianProcessRegressor

# Create GPR model
gpr = GaussianProcessRegressor(
    normalize_y=True,
    random_state=42
)

# Train model
gpr.fit(
    X,
    y
)

print()
print("GPR MODEL TRAINED")

# Select features for prediction
# WHY: GPR only needs the features used during training
prediction_features = lhs_catalysts[
    [
        "Ni_fraction",
        "Co_fraction",
        "Fe_fraction"
    ]
]

# Predict overpotential and uncertainty
prediction, uncertainty = gpr.predict(
    prediction_features,
    return_std=True
)

# Store predictions
lhs_catalysts["Predicted_Overpotential"] = prediction

# Store uncertainty
lhs_catalysts["Uncertainty"] = uncertainty

print()
print("FIRST 10 PREDICTIONS")
print(
    lhs_catalysts[
        [
            "Ni_fraction",
            "Co_fraction",
            "Fe_fraction",
            "Predicted_Overpotential",
            "Uncertainty"
        ]
    ].head(10)
)

lhs_catalysts.to_csv(
    "results/predicted_lhs_500_catalysts.csv",
    index=False
)

print()
print("Predicted LHS catalysts saved successfully.")