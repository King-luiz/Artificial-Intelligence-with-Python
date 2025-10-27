# model.py
# Bayesian Network for Rain, Maintenance, Train, and Appointment
# Compatible with pomegranate >= 1.0.0

from pomegranate import BayesianNetwork
import numpy as np

# Define the conditional probability tables using dictionaries
# Variables: rain, maintenance, train, appointment

# Rain probabilities
rain_probs = {
    "none": 0.7,
    "light": 0.2,
    "heavy": 0.1
}

# Maintenance depends on rain
maintenance_probs = {
    "none": {"yes": 0.4, "no": 0.6},
    "light": {"yes": 0.2, "no": 0.8},
    "heavy": {"yes": 0.1, "no": 0.9}
}

# Train depends on rain and maintenance
train_probs = {
    ("none", "yes"): {"on time": 0.8, "delayed": 0.2},
    ("none", "no"): {"on time": 0.9, "delayed": 0.1},
    ("light", "yes"): {"on time": 0.6, "delayed": 0.4},
    ("light", "no"): {"on time": 0.7, "delayed": 0.3},
    ("heavy", "yes"): {"on time": 0.4, "delayed": 0.6},
    ("heavy", "no"): {"on time": 0.5, "delayed": 0.5}
}

# Appointment depends on train
appointment_probs = {
    "on time": {"attend": 0.9, "miss": 0.1},
    "delayed": {"attend": 0.6, "miss": 0.4}
}

# Define the model structure
structure = (
    "rain -> maintenance -> train -> appointment",
    "rain -> train"
)

# Build model using the new API
# Note: In the new API, we provide data samples to learn structure or specify manually.

# For simplicity, we create a mock dataset consistent with our structure
data = np.array([
    ["none", "no", "on time", "attend"],
    ["none", "yes", "delayed", "attend"],
    ["light", "yes", "delayed", "miss"],
    ["heavy", "no", "on time", "attend"],
    ["heavy", "yes", "delayed", "miss"]
])

# Initialize and fit the Bayesian Network
model = BayesianNetwork.from_samples(data, algorithm='exact', state_names=["rain", "maintenance", "train", "appointment"])
