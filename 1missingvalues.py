total_records = len(data)
missing_counts = {"firstName": 0, "lastName": 0, "birthDate": 0}

for record in data:
    patient = record.get("patientDetails", {})
    if not patient.get("firstName"):
        missing_counts["firstName"] += 1
    if not patient.get("lastName"):
        missing_counts["lastName"] += 1
    if not patient.get("birthDate"):
        missing_counts["birthDate"] += 1

missing_percentages = {col: (count / total_records) * 100 for col, count in missing_counts.items()}
