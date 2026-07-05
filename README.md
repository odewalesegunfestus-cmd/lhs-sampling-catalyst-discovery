# LHS Sampling Catalyst Discovery

This repository demonstrates Latin Hypercube Sampling (LHS) for efficient virtual catalyst generation in AI-driven catalyst discovery.

## Workflow

LHS Sampling  
↓  
Generate 500 Virtual Catalysts  
↓  
Normalize Ni-Co-Fe Fractions  
↓  
Train GPR Model  
↓  
Predict Overpotential  
↓  
Estimate Uncertainty  
↓  
Calculate EI Score  
↓  
Rank Top Catalyst Candidates  

## Key Outputs

- `results/lhs_500_realistic_catalysts.csv`
- `results/predicted_lhs_500_catalysts.csv`
- `results/ranked_lhs_candidates.csv`
- `figures/lhs_distribution.png`
- `figures/grid_vs_lhs.png`
- `figures/top10_lhs_candidates.png`

## Tools Used

- Python
- Pandas
- SciPy
- Scikit-learn
- Matplotlib

## Author

Odewale Segun Festus