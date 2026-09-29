import json
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

from triage import train_classifier, set_classifier, classify_email


DATA_FILE = Path(__file__).parent / "data" / "emails.json"
METRICS_FILE = Path(__file__).parent / "metrics.json"

LABELS = ["order", "feedback", "support", "other"]


def load_dataset():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def main():
    data = load_dataset()

    texts = [item["text"] for item in data]
    labels = [item["label"] for item in data]

    # Split the labeled dataset into training and testing sets.
    X_train, X_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.20,
        random_state=42,
        stratify=labels
    )

    print(f"Total emails: {len(data)}")
    print(f"Training emails: {len(X_train)}")
    print(f"Testing emails: {len(X_test)}")

    # Train the classifier using only the training data.
    model = train_classifier(X_train, y_train)

    # Tell triage.py to use the trained model.
    set_classifier(model)

    predictions = []
    confidences = []

    # Run the classification function on every test email.
    for email in X_test:
        result = classify_email(email)

        predictions.append(result["category"])
        confidences.append(result["confidence"])

    # Calculate overall accuracy.
    accuracy = accuracy_score(y_test, predictions)

    # Calculate precision, recall and F1 per class.
    report = classification_report(
        y_test,
        predictions,
        labels=LABELS,
        output_dict=True,
        zero_division=0
    )

    metrics = {
        "accuracy": round(float(accuracy), 4),
        "train_samples": len(X_train),
        "test_samples": len(X_test),
        "classes": {}
    }

    for label in LABELS:
        metrics["classes"][label] = {
            "precision": round(report[label]["precision"], 4),
            "recall": round(report[label]["recall"], 4),
            "f1": round(report[label]["f1-score"], 4)
        }

    metrics["uncertain_predictions"] = predictions.count("Uncertain")

    with METRICS_FILE.open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=4)

    print("\nEvaluation Results")
    print("------------------")

    for label in LABELS:
        values = metrics["classes"][label]

        print(
            f"{label}: "
            f"precision={values['precision']}, "
            f"recall={values['recall']}, "
            f"F1={values['f1']}"
        )

    print(f"\nAccuracy: {metrics['accuracy']}")
    print(f"Uncertain predictions: {metrics['uncertain_predictions']}")

    if accuracy >= 0.80:
        print("\nAccuracy requirement PASSED.")
    else:
        print("\nAccuracy requirement FAILED.")


if __name__ == "__main__":
    main()
