# likelihood.py
# Uses the Bayesian model from model.py to compute probability of an event

from model import model
import numpy as np

# Define the observation
observation = np.array([["none", "no", "on time", "attend"]])

# Compute log probability (new API uses log_probability)
log_prob = model.log_probability(observation)

# Convert to regular probability
probability = np.exp(log_prob[0])

print(f"Probability of observation {observation.tolist()[0]} = {probability:.6f}")
