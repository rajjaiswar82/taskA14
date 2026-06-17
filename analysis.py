import pandas as pd

df = pd.read_csv("data/monitoring_data.csv" )

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Candidate IDs:")
print(df.duplicated(subset=["candidate_id"]).sum())

print("Average Risk Score:", df["risk_score"].mean())

print("\nHighest Risk Candidate:")
print(df.loc[df["risk_score"].idxmax()])

print("\nCandidate Recommendations")
print("\nTotal Candidates:", len(df))

print("\nAverage Session Duration:")
print(df["session_duration"].mean())

print("\nTotal Candidates With Phone Detection:")
print(df["phone_detected"].sum())

print("\nTotal Candidates With Multiple Faces:")
print(df["multiple_faces"].sum())

print("\nTotal Candidates With Audio Anomaly:")
print(df["audio_anomaly"].sum())

for _, row in df.iterrows():

    if row["risk_score"] >= 70:
        recommendation = "Not Allowed for Next Stage"

    else:
        recommendation = "Allowed for Next Stage"

    print(
        f"Candidate {row['candidate_id']} "
        f"| Risk Score: {row['risk_score']} "
        f"| {recommendation}"
    )
    