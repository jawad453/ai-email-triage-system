import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "emails.json"
ALLOWED_LABELS = {"order", "feedback", "support", "other"}


def load_data():
    """Load the email dataset from the JSON file."""
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def validate_data(data):
    """Validate the required structure and labels."""
    errors = []

    if not isinstance(data, list):
        errors.append("Dataset must be a JSON array.")
        return errors

    if len(data) < 200:
        errors.append(
            f"Dataset contains only {len(data)} entries; at least 200 are required."
        )

    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            errors.append(f"Entry {index} must be a JSON object.")
            continue

        if "text" not in item:
            errors.append(f"Entry {index} is missing the 'text' field.")
        elif not isinstance(item["text"], str) or not item["text"].strip():
            errors.append(f"Entry {index} has an invalid 'text' field.")

        if "label" not in item:
            errors.append(f"Entry {index} is missing the 'label' field.")
        elif item["label"] not in ALLOWED_LABELS:
            errors.append(
                f"Entry {index} has invalid label '{item['label']}'. "
                f"Allowed labels: {', '.join(sorted(ALLOWED_LABELS))}."
            )

    return errors


def print_summary(data):
    """Print the total number of emails and label distribution."""
    counts = {label: 0 for label in sorted(ALLOWED_LABELS)}

    for item in data:
        if isinstance(item, dict) and item.get("label") in counts:
            counts[item["label"]] += 1

    print("\nDataset Summary")
    print("-" * 30)
    print(f"Total emails: {len(data)}")

    for label, count in counts.items():
        print(f"{label}: {count}")


def main():
    try:
        data = load_data()
    except FileNotFoundError:
        print(f"ERROR: Dataset not found at: {DATA_FILE}")
        return
    except json.JSONDecodeError as error:
        print(f"ERROR: Invalid JSON file: {error}")
        return

    errors = validate_data(data)

    if errors:
        print("Dataset validation FAILED.")
        print("\nProblems found:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Dataset validation PASSED.")

    print_summary(data)


if __name__ == "__main__":
    main()
