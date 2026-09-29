import json
import time

from triage import train_classifier, set_classifier, classify_email


DATA_FILE = "data/emails.json"


def main():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    texts = [item["text"] for item in data]
    labels = [item["label"] for item in data]

    # Train once before timing the classification calls.
    model = train_classifier(texts, labels)
    set_classifier(model)

    test_email = "I want to know the status of my coffee order."

    calls = 50
    start = time.perf_counter()

    for _ in range(calls):
        classify_email(test_email)

    end = time.perf_counter()

    total_time = end - start
    average_time = total_time / calls

    print("Load Test")
    print("---------")
    print(f"Calls: {calls}")
    print(f"Total time: {total_time:.4f} seconds")
    print(f"Average response time: {average_time:.6f} seconds")

    if average_time < 0.5:
        print("PASS: Average latency is below 0.5 seconds.")
    else:
        print("FAIL: Average latency is 0.5 seconds or higher.")


if __name__ == "__main__":
    main()
