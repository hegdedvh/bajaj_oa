age_groups = {"Child": 0, "Teen": 0, "Adult": 0, "Senior": 0}
for record in data:
    birth_date = record.get("patientDetails", {}).get("birthDate")
    age = calculate_age(birth_date)
    age_group = get_age_group(age)
    if age_group:
        age_groups[age_group] += 1
adult_count = age_groups["Adult"]
