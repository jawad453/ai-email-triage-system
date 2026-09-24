import json
from pathlib import Path


CONFIDENCE_THRESHOLD = 0.6
ALLOWED_CATEGORIES = {"order", "feedback", "support", "other"}


def load_prompt():
    """Load the reusable classification prompt."""
    prompt_path = Path(__file__).parent / "prompt.txt"
    return prompt_path.read_text(encoding="utf-8")


def mock_llm(email_text):
    """
    Mock LLM used for local testing.

    In the real application, this function can be replaced
    with an OpenAI API call.
    """

    text = email_text.lower()

    # Simulate a low-confidence response
    if "not sure" in text:
        return json.dumps({
            "category": "support",
            "confidence": 0.45
        })

    # Simulate prompt-injection handling
    if "ignore previous instructions" in text:
        return json.dumps({
            "category": "other",
            "confidence": 0.91
        })

    if any(word in text for word in ["order", "ordered", "delivery"]):
        return json.dumps({
            "category": "order",
            "confidence": 0.92
        })

    if any(word in text for word in ["feedback", "great", "excellent", "complaint"]):
        return json.dumps({
            "category": "feedback",
            "confidence": 0.88
        })

    if any(word in text for word in ["problem", "issue", "help", "broken"]):
        return json.dumps({
            "category": "support",
            "confidence": 0.84
        })

    return json.dumps({
        "category": "other",
        "confidence": 0.72
    })


def classify_email(email_text):
    """
    Classify an email and apply the confidence threshold.

    Returns:
        dict: JSON-compatible object containing category and confidence.
    """

    if not isinstance(email_text, str):
        raise TypeError("email_text must be a string")

    if not email_text.strip():
        return {
            "category": "Uncertain",
            "confidence": 0.0
        }

    prompt = load_prompt()

    # Replace the placeholder with the customer's email.
    final_prompt = prompt.replace("{{EMAIL_TEXT}}", email_text)

    # The prompt is constructed for the LLM.
    # The mock does not need the prompt itself, but a real API call would use it.
    _ = final_prompt

    response = mock_llm(email_text)

    try:
        result = json.loads(response)
    except json.JSONDecodeError as exc:
        raise ValueError("LLM returned invalid JSON") from exc

    if "category" not in result or "confidence" not in result:
        raise ValueError("LLM response must contain category and confidence")

    category = result["category"]
    confidence = result["confidence"]

    if not isinstance(category, str):
        raise ValueError("category must be a string")

    if not isinstance(confidence, (int, float)):
        raise ValueError("confidence must be a number")

    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0.0 and 1.0")

    if category not in ALLOWED_CATEGORIES:
        category = "other"

    # Required assignment rule:
    # confidence below 0.6 -> Uncertain
    if confidence < CONFIDENCE_THRESHOLD:
        category = "Uncertain"

    return {
        "category": category,
        "confidence": confidence
    }


if __name__ == "__main__":
    test_emails = [
        "I want to know the status of my coffee order.",
        "Your coffee was excellent. I really enjoyed it.",
        "My order arrived damaged. Please help.",
        "I am not sure what category this email belongs to."
    ]

    for email in test_emails:
        result = classify_email(email)

        print("Email:", email)
        print("Result:", json.dumps(result))
        print()
