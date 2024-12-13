active_count = 0
inactive_count = 0
for record in data:
    for med in record.get("consultationData", {}).get("medicines", []):
        if med["isActive"]:
            active_count += 1
        else:
            inactive_count += 1
total_medicines = active_count + inactive_count
active_percentage = (active_count / total_medicines) * 100 if total_medicines else 0
inactive_percentage = (inactive_count / total_medicines) * 100 if total_medicines else 0
