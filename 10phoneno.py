valid_mobile_count = 0
for record in data:
    phone_number = record.get("phoneNumber", "")
    if is_valid_mobile(phone_number):
        valid_mobile_count += 1

results = {
    "missing_percentages": {k: round(v, 2) for k, v in missing_percentages.items()},
    "female_percentage": round(female_percentage, 2),
    "adult_count": adult_count,
    "average_medicines": round(average_medicines, 2),
    "third_most_frequent_medicine": third_most_frequent_medicine,
    "medicine_distribution": (round(active_percentage, 2), round(inactive_percentage, 2)),
    "valid_mobile_count": valid_mobile_count,
}

ages = []
medicine_counts = []
for record in data:
    birth_date = record.get("patientDetails", {}).get("birthDate")
    age = calculate_age(birth_date)
    medicines = record.get("consultationData", {}).get("medicines", [])
    if age is not None:
        ages.append(age)
        medicine_counts.append(len(medicines))

if ages and medicine_counts:
    pearson_corr, _ = pearsonr(ages, medicine_counts)
    pearson_corr = round(pearson_corr, 2)
else:
    pearson_corr = None

results["pearson_correlation"] = pearson_corr
print(results)
