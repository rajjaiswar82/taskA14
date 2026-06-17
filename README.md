# Monitoring Analytics Dataset Generator

## Project Overview

This project is a part of the AI Interview Monitoring System. The objective is to create a sample monitoring dataset and perform basic analytics on candidate interview monitoring data.

The project demonstrates:

* Dataset creation
* Data dictionary definition
* Risk score analysis
* Candidate recommendation for the next stage
* Handling of edge cases such as missing values and duplicate candidates

---

## Project Structure

```text
task14/
│
├── monitoring_data.csv
├── data_dictionary.py
├── analysis.py
└── README.md
```

---

## Dataset Columns

| Column Name       | Description                              | Data Type |
| ----------------- | ---------------------------------------- | --------- |
| candidate_id      | Unique candidate identifier              | int       |
| risk_score        | Candidate risk score (0-100)             | int       |
| suspicious_events | Number of suspicious activities detected | int       |
| session_duration  | Interview duration in minutes            | int       |
| phone_detected    | Phone detected during interview          | bool      |
| multiple_faces    | Multiple faces detected during interview | bool      |
| audio_anomaly     | Suspicious audio activity detected       | bool      |

---

## Analytics Performed

The analysis script performs:

* Average risk score calculation
* Highest risk candidate identification
* Total candidate count
* Average session duration
* Phone detection analysis
* Multiple face detection analysis
* Audio anomaly analysis
* Candidate recommendation for next stage

### Recommendation Logic

* Risk Score < 70 → Allowed for Next Stage
* Risk Score ≥ 70 → Not Allowed for Next Stage

---

## Edge Cases Handled

### Missing Records

The analysis checks for missing values using:

```python
df.isnull().sum()
```

### Duplicate Candidates

The analysis checks for duplicate candidate IDs using:

```python
df.duplicated(subset=["candidate_id"]).sum()
```

---

## How to Run


Run the analytics script:

```bash
python analysis.py
```

---

## Sample Output

```text
Average Risk Score: 62.0

Highest Risk Candidate:
Candidate ID: 124
Risk Score: 95

Total Candidates: 30

Average Session Duration: 49.13

Total Candidates With Phone Detection: 17

Total Candidates With Multiple Faces: 8

Total Candidates With Audio Anomaly: 11
```

---


