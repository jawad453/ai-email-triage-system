import json
import re

from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC


CONFIDENCE_THRESHOLD = 0.6

ALLOWED_CATEGORIES = {
    "order",
    "feedback",
    "support",
    "other",
}

trained_classifier = None


def train_classifier(texts, labels):
    """
    Train and return the email classification model.
    """

    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                ngram_range=(1, 2),
                sublinear_tf=True
            )
        ),
        (
            "classifier",
            CalibratedClassifierCV(
                LinearSVC(),
                cv=3
            )
        )
    ])

    model.fit(texts, labels)

    return model


def set_classifier(model):
    """
    Set the trained classifier used by classify_email().
    """
    global trained_classifier
    trained_classifier = model


def sanitize_email(email_text):
    """
    Remove common prompt-injection instruction from the email.
    The email is treated as untrusted data.
    """

    cleaned_text = re.sub(
        r"(?i)\bignore\s+previous\s+instructions\b[.!]?\s*",
        "",
        email_text
    )

    return cleaned_text.strip()


def classify_email(email_text):
    """
    Classify an email and return:
    {
        "category": "...",
        "confidence": 0.0
    }

    Confidence below 0.6 results in 'Uncertain'.
    """

    if not isinstance(email_text, str):
        raise TypeError("email_text must be a string")

    if not email_text.strip():
        return {
            "category": "Uncertain",
            "confidence": 0.0
        }

    # Treat the email as untrusted input.
    email_text = sanitize_email(email_text)

    if not email_text:
        return {
            "category": "Uncertain",
            "confidence": 0.0
        }

    if trained_classifier is None:
        raise RuntimeError(
            "No classifier has been trained. "
            "Call train_classifier() and set_classifier() first."
        )

    probabilities = trained_classifier.predict_proba([email_text])[0]

    classes = trained_classifier.classes_

    best_index = probabilities.argmax()
    category = classes[best_index]
    confidence = float(probabilities[best_index])

    if category not in ALLOWED_CATEGORIES:
        category = "other"

    if confidence < CONFIDENCE_THRESHOLD:
        category = "Uncertain"

    return {
        "category": category,
        "confidence": round(confidence, 4)
    }


if __name__ == "__main__":
    print("triage.py is ready for Task 3.")
    print("The classifier will be trained by evaluation.py.")
