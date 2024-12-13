total_medicines = 0
for record in data:
    medicines = record.get("consultationData", {}).get("medicines", [])
    total_medicines += len(medicines)
average_medicines = total_medicines / total_records

# Question 5: 3rd most frequently prescribed medicine name
medicine_counter = Counter(
    med["medicineName"]
    for record in data
    for med in record.get("consultationData", {}).get("medicines", [])
)
third_most_frequent_medicine = medicine_counter.most_common(3)[-1][0]
