# AI-Powered Email Triage System for Brew & Bean Cafe

An AI-powered email classification and triage system for **Brew & Bean Cafe**. The project is designed to automatically classify customer emails into the appropriate category, support consistent routing, and provide a foundation for handling uncertain cases.

## Project Information

- **Intern:** Jawad Afsar
- **Technology:** Artificial Intelligence
- **Client:** Brew & Bean Cafe
- **Level:** Intermediate
- **Project Duration:** 20 September 2026 – 11 October 2026
- **Main Categories:** `order`, `feedback`, `support`, `other`

## Project Goal

Brew & Bean Cafe receives customer emails covering orders, feedback, and support requests. The goal is to reduce manual sorting time by building an automated email classification service that routes messages to the appropriate staff member and provides a fallback for uncertain cases.

## Planned Deliverables

The complete project is organized into five tasks:

1. **Labeled email dataset** with at least 200 examples.
2. **Reusable LLM prompt and Python classification module.**
3. **Automated evaluation** with precision/recall reporting and a test suite.
4. **Dockerized FastAPI service** with CI/CD and deployment to a free hosting URL.
5. **Handover documentation and demo package**, including cost estimate, limitations, and demo video.

## Repository Structure

The repository will contain the following structure as the project progresses:

```text
ai-email-triage-system/
│
├── data/
│   └── emails.json
│
├── labeling_guide.md
├── load_data.py
│
├── prompt/
│   └── classification_prompt.md
│
├── src/
│   └── classifier.py
│
├── tests/
│   └── ...
│
├── evaluation/
│   └── ...
│
├── app/
│   └── ...
│
├── Dockerfile
├── requirements.txt
├── README.md
└── ...
```

> The exact folders and files will be added as each project task is completed.

---

# Task 1 — Create and Label Sample Email Dataset

## Dataset

The dataset is stored in:

```text
data/emails.json
```

It contains more than the required 200 customer email examples. Each record contains the required `text` and `label` fields:

```json
{
  "text": "I would like to order two large cappuccinos.",
  "label": "order"
}
```

The four allowed labels are:

- `order`
- `feedback`
- `support`
- `other`

The dataset is designed around realistic customer communication with a coffee-shop context.

## Labeling Guide

The labeling rules are documented in:

```text
labeling_guide.md
```

The guide explains each category and provides rules for distinguishing similar cases, such as an order request versus a support issue.

## Dataset Validation

The Python validation script is:

```text
load_data.py
```

It is responsible for loading the JSON dataset, checking the required structure and labels, and printing a summary of the dataset.

## Task 1 Requirements

The project brief specifies that Task 1 should include:

- `data/emails.json` with at least 200 entries
- `text` and `label` fields for each entry
- Balanced labels across the four categories
- `labeling_guide.md`
- `load_data.py` that runs without error and prints a summary

---

# Task 2 — LLM Prompt and Classification Module

The second task will provide a reusable prompt for classifying incoming Brew & Bean Cafe emails.

The classification system will:

1. Receive a customer email.
2. Analyze the main purpose of the message.
3. Assign exactly one category.
4. Return structured output suitable for use by the Python application.
5. Handle unclear cases according to the project's fallback rules.

Planned files:

```text
prompt/classification_prompt.md
src/classifier.py
```

The classification logic will avoid inventing information that is not present in the email.

---

# Task 3 — Automated Evaluation

The classification system will be evaluated against labeled test data.

The evaluation stage will include:

- Automated test cases
- Precision measurement
- Recall measurement
- Category-level results
- Error analysis
- Performance checks
- Basic security checks

The evaluation results will be documented in the repository once Task 3 is completed.

---

# Task 4 — FastAPI, Docker and CI/CD

The project will be exposed as an API so that another application can send an email and receive its classification.

The planned service will include:

- FastAPI application
- API endpoint for email classification
- Docker configuration
- Dependency configuration
- CI/CD pipeline
- Deployment to a free hosting service

The deployed service URL will be added here after deployment:

```text
Deployment URL: [To be added]
```

---

# Task 5 — Handover Documentation and Demo

The final project package will include:

- Setup instructions
- Usage instructions
- Architecture/project overview
- Cost estimate
- Known limitations
- Future improvements
- Demo video link

### Demo Video

```text
Demo video: [To be added]
```

### Cost Estimate

The final cost estimate will document the expected costs of using the selected AI/API and hosting services, including any free-tier limitations.

### Limitations

The final limitations section will document known issues such as:

- Ambiguous customer messages
- Classification errors
- Dependence on the selected LLM/API
- API availability and rate limits
- Potential changes in model behavior
- Cases requiring human review

---

# Classification Categories

| Category | Purpose |
|---|---|
| `order` | Messages about placing, changing, or cancelling an order. |
| `feedback` | Customer opinions, reviews, compliments, complaints, or comments about their experience when no specific support resolution is requested. |
| `support` | Problems or issues where the customer needs help or a resolution. |
| `other` | General questions or messages that do not fit the other three categories. |

The complete labeling rules are available in `labeling_guide.md`.

---

# Example

### Input

```text
Hi, I would like to order two large cappuccinos and one blueberry muffin for pickup at 5 PM.
```

### Expected Classification

```json
{
  "label": "order"
}
```

---

# Development Approach

The project is being completed one task at a time, with each task building on the previous task:

```text
Dataset
   ↓
Labeling Guide
   ↓
Validation
   ↓
LLM Prompt
   ↓
Classification Module
   ↓
Automated Evaluation
   ↓
FastAPI Service
   ↓
Docker + CI/CD
   ↓
Deployment
   ↓
Documentation + Demo
```

This approach keeps the dataset, classification logic, evaluation, deployment, and documentation connected throughout the project.

---

# How to Run Task 1

After cloning the repository, make sure Python is installed.

Run:

```bash
python load_data.py
```

The script should load `data/emails.json`, validate the dataset structure, and print a summary of the labels.

---

# Future Improvements

Potential future improvements include:

- Confidence scoring for classifications
- Human review for uncertain emails
- Priority detection for urgent messages
- More detailed routing rules
- Additional evaluation data
- Monitoring classification performance after deployment
- Integration with the cafe's email workflow

---

# Project Status

| Task | Description | Status |
|---|---|---|
| Task 1 | Create and label sample email dataset | In progress / files being submitted |
| Task 2 | LLM prompt and classification function | Planned |
| Task 3 | Automated evaluation and security checks | Planned |
| Task 4 | FastAPI, Docker, CI/CD and deployment | Planned |
| Task 5 | Documentation, cost estimate and demo package | Planned |

The repository will be updated as each task is completed and reviewed.

---

# Submission

This repository is the main project workspace for the **AI-Powered Email Triage System for Brew & Bean Cafe**.

Each task will be developed, tested, and committed separately so that the project history shows the progression from the initial dataset through the final deployed service.

## Author

**Jawad Afsar**

Artificial Intelligence Intern
