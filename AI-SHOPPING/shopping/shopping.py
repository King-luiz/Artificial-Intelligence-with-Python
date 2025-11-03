import csv
import sys
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4

# Mapping for month abbreviations to integers
MONTHS = {
    "Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3, "May": 4, "June": 5,
    "Jul": 6, "Aug": 7, "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11
}


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data.csv")

    # Load data from CSV
    evidence, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)

    # Evaluate results
    sensitivity, specificity = evaluate(y_test, predictions)
    correct = (y_test == predictions).sum()
    incorrect = len(y_test) - correct

    # Print results
    print(f"Correct: {correct}")
    print(f"Incorrect: {incorrect}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file and convert into evidence lists and labels.
    Return (evidence, labels).
    """
    evidence = []
    labels = []

    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Prepare evidence (17 features)
            evidence.append([
                int(row["Administrative"]),
                float(row["Administrative_Duration"]),
                int(row["Informational"]),
                float(row["Informational_Duration"]),
                int(row["ProductRelated"]),
                float(row["ProductRelated_Duration"]),
                float(row["BounceRates"]),
                float(row["ExitRates"]),
                float(row["PageValues"]),
                float(row["SpecialDay"]),
                MONTHS[row["Month"]],
                int(row["OperatingSystems"]),
                int(row["Browser"]),
                int(row["Region"]),
                int(row["TrafficType"]),
                1 if row["VisitorType"] == "Returning_Visitor" else 0,
                1 if row["Weekend"] == "TRUE" else 0,
            ])
            # Prepare label
            labels.append(1 if row["Revenue"] == "TRUE" else 0)

    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given evidence and labels, train a k-nearest neighbor model (k=1).
    Return the trained model.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and predicted labels,
    return (sensitivity, specificity).
    sensitivity = true positive rate
    specificity = true negative rate
    """
    true_positives = 0
    true_negatives = 0
    positives = 0
    negatives = 0

    for actual, predicted in zip(labels, predictions):
        if actual == 1:
            positives += 1
            if predicted == 1:
                true_positives += 1
        else:
            negatives += 1
            if predicted == 0:
                true_negatives += 1

    sensitivity = true_positives / positives if positives else 0
    specificity = true_negatives / negatives if negatives else 0

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
