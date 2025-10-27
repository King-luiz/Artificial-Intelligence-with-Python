
# 🧩 Bayesian Networks – Modeling Uncertainty (CS50 AI)

This project demonstrates how **Bayesian Networks** can be used to represent and reason about uncertainty using **probability theory** in Python.  
It is based on **Lecture 2: Uncertainty** from [Harvard University’s CS50 Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2020/).

---

## 📘 Project Overview

This mini-project models a real-world scenario involving weather, train delays, and appointments using a **Bayesian Network** built with the `pomegranate` library.

The network models dependencies between the following variables:

| Variable | Description |
|-----------|--------------|
| **Rain** | Weather condition (none, light, heavy) |
| **Maintenance** | Whether maintenance is scheduled (yes/no) |
| **Train** | Train arrival status (on time/delayed) |
| **Appointment** | Whether a person attends or misses an appointment |

By defining conditional probability tables (CPTs) and using probabilistic inference, we can predict outcomes, calculate likelihoods, and sample random events based on given evidence.

---

## 🧱 Folder Structure

Bayesnet/
│
├── model.py # Defines the Bayesian Network structure and relationships
├── inference.py # Performs probabilistic inference given some evidence
├── likelihood.py # Calculates the probability of specific observations
└── sample.py # Generates random samples using rejection sampling

yaml
Copy code

---

## ⚙️ Requirements

Make sure you have **Python 3.8+** installed.  
Install the required package:

```bash
pip install pomegranate numpy
```

▶️ How to Run
## 1. Model Construction
Run model.py to initialize the Bayesian network:
```
---
```
bash
Copy code
python model.py
```
This builds the model using sample data consistent with the designed dependencies.
```
## 2. Inference
Predict probabilities of all nodes given some evidence:

bash
Copy code
python inference.py
Example Output:

yaml
Copy code
rain
    none: 0.7040
    light: 0.2040
    heavy: 0.0920
maintenance
    yes: 0.2331
    no: 0.7669
train
    on time: 0.0000
    delayed: 1.0000
appointment
    attend: 0.5930
    miss: 0.4070
## 3. Likelihood Calculation
Compute the probability of a specific observation:
```
bash
Copy code
python likelihood.py
```
Example Output:

nginx
Copy code
Probability of observation ['none', 'no', 'on time', 'attend'] = 0.083333

## 4. Rejection Sampling
Estimate the probability distribution of appointments given that the train was delayed:

bash
Copy code
python sample.py
Example Output:

yaml
Copy code
Counter({'attend': 6004, 'miss': 3996})
## 📊 Concepts Covered
Probability and uncertainty

Conditional Probability Tables (CPTs)

Bayesian Networks

Inference and prediction

Sampling and rejection sampling

Pomegranate’s probabilistic modeling API

## 🧩 Libraries Used
pomegranate – Probabilistic models and Bayesian networks

NumPy – Array operations and probability computation

Collections – Data counting for sampling results

## 📚 References
Harvard University CS50 AI – Lecture 2: Uncertainty
https://cs50.harvard.edu/ai/2020/

## 👨‍💻 Author
= Lewins Mureithi Nderitu
= Web Developer & AI Learner

. 📞 Phone: +254 112876340
. 📧 Email: mureithilewins@gmail.com
. 🌐 GitHub: King-luiz

🏁 License
This project is for educational purposes under the MIT License.
You are free to use, modify, and distribute it for learning and non-commercial use.
