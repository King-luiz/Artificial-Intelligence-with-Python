# 1.Knowledge


# Logic-Based AI Projects

This repository contains a collection of Python projects demonstrating knowledge representation and reasoning using propositional logic. These projects implement AI agents that can draw conclusions from existing knowledge using logical inference.

## 📚 Overview

The projects showcase how AI systems can represent knowledge and perform logical reasoning to solve problems, similar to how humans draw conclusions from existing information. The implementation uses propositional logic with model checking algorithms to determine what can be inferred from given facts.

## 🧠 Concepts Covered

### Core Logical Concepts
- **Knowledge-Based Agents**: Agents that reason using internal representations of knowledge
- **Propositional Logic**: Using propositions that can be true or false
- **Logical Connectives**: AND (∧), OR (∨), NOT (¬), IMPLICATION (→), BICONDITIONAL (↔)
- **Model Checking**: Algorithm for determining logical entailment
- **Inference**: Deriving new sentences from existing ones

### Key Components
- **Symbols**: Represent atomic propositions
- **Sentences**: Logical assertions about the world
- **Knowledge Base**: Collection of known sentences
- **Entailment**: Relationship where if α is true, β must also be true

## 📁 Project Structure

### Core Files
- `logic.py` - The main logic engine containing classes for logical operations and model checking
- `knowledge.py` - Basic example of building a knowledge base
- `harry.py` - Harry Potter themed logic puzzle
- `clue.py` - Implementation of Clue game logic
- `mastermind.py` - Mastermind game solver using logic
- `puzzle.py` - Hogwarts house assignment puzzle

## 🔧 Implementation Details

### Logic Engine (`logic.py`)
The core logic system implements:

- **Sentence Classes**: `Symbol`, `Not`, `And`, `Or`, `Implication`, `Biconditional`
- **Model Checking**: Recursive algorithm that checks all possible truth assignments
- **Evaluation**: Determining truth values in different models

Key methods:
- `evaluate(model)`: Checks if sentence is true in given model
- `formula()`: Returns human-readable logical formula
- `symbols()`: Returns all symbols in the sentence
- `model_check(knowledge, query)`: Determines if knowledge entails query

## 🎯 Project Examples

### 1. Harry Potter Puzzle (`harry.py`)
**Problem**: Determine if it rained based on:
- If it didn't rain, Harry visited Hagrid
- Harry visited Hagrid or Dumbledore, but not both  
- Harry visited Dumbledore

**Solution**: Using logical inference to conclude it must have rained.

### 2. Clue Game (`clue.py`)
**Problem**: Deduce the murderer, weapon, and location in a Clue-like game given:
- Initial known cards
- Other players' guesses and responses
- Game rules (exactly one person, weapon, location)

**Solution**: Model checking to eliminate possibilities and find the solution.

### 3. Mastermind Solver (`mastermind.py`)
**Problem**: Determine the correct color sequence based on feedback about correct positions.

**Solution**: Representing color-position combinations and using logical constraints to find valid solutions.

### 4. Hogwarts House Assignment (`puzzle.py`)
**Problem**: Assign four people to four houses given constraints about who can be in which house.

**Solution**: Using first-order logic concepts to represent relationships and constraints.

## 🚀 Usage

### Running the Projects

1. **Basic Knowledge Base**:
   ```bash
   python knowledge.py
   ```

2. **Harry Potter Logic**:
   ```bash
   python harry.py
   ```

3. **Clue Game**:
   ```bash
   python clue.py
   ```

4. **Mastermind Solver**:
   ```bash
   python mastermind.py
   ```

5. **House Assignment Puzzle**:
   ```bash
   python puzzle.py
   ```

### Creating Your Own Logic Problems

```python
from logic import *

# Define symbols
rain = Symbol("rain")
sunny = Symbol("sunny")

# Build knowledge base
knowledge = And(
    Implication(rain, Not(sunny)),
    Or(rain, sunny),
    Not(And(rain, sunny))
)

# Check entailment
print(model_check(knowledge, rain))
```

## 📖 Learning Outcomes

Through these projects, you'll understand:

1. How AI represents knowledge using logical sentences
2. The process of logical inference and deduction
3. Model checking algorithms for determining entailment
4. Practical applications of logic in problem-solving
5. Knowledge engineering - representing real-world problems logically

## 🛠 Requirements

- Python 3.6+
- `termcolor` library (for colored output in clue.py)

Install dependencies:
```bash
pip install termcolor
```

## 🔍 Key Algorithms

### Model Checking Algorithm
The recursive model checking algorithm works by:

1. Enumerating all possible truth assignments to propositional symbols
2. Checking if the knowledge base is true in each model
3. Verifying that the query is also true in all models where KB is true
4. Using recursion to efficiently explore the space of possible models

## 💡 Extensions

Possible enhancements to these projects:

- Add more complex inference rules
- Implement resolution-based inference
- Add support for first-order logic
- Create interactive versions of the games
- Optimize the model checking algorithm
- Add unit tests for logical operations

This collection demonstrates the fundamental principles of knowledge representation and reasoning in artificial intelligence, providing a practical foundation for building more sophisticated AI systems.
