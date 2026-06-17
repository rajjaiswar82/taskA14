DATA_DICTIONARY = {
    "candidate_id": {
        "datatype": "int",
        "description": "Unique candidate identifier"
    },
    "risk_score": {
        "datatype": "int",
        "description": "Risk score from 0 to 100"
    },
    "suspicious_events": {
        "datatype": "int",
        "description": "Number of suspicious activities"
    },
    "session_duration": {
        "datatype": "int",
        "description": "Interview duration in minutes"
    },
    "phone_detected": {
        "datatype": "bool",
        "description": "Phone detected during interview"
    },
    "multiple_faces": {
        "datatype": "bool",
        "description": "Multiple faces detected"
    },
    "audio_anomaly": {
        "datatype": "bool",
        "description": "Suspicious audio detected"
    }
}

print(DATA_DICTIONARY)