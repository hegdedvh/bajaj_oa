with open('/mnt/data/DataEngineeringQ2.json', 'r') as f:
    full_data = json.load(f)

data_cleaned = []
for record in full_data:
    birth_date = record.get('patientDetails', {}).get('birthDate', None)
    medicines = record.get('consultationData', {}).get('medicines', [])
    if birth_date:
        try:
            birth_year = int(birth_date[:4])
            age = current_year - birth_year
        except (ValueError, TypeError):
            age = None
    else:
        age = None
    num_medicines = len(medicines)
    if age is not None:
        data_cleaned.append({"age": age, "num_medicines": num_medicines})

df_cleaned = pd.DataFrame(data_cleaned)
if not df_cleaned.empty:
    pearson_corr, _ = pearsonr(df_cleaned['age'], df_cleaned['num_medicines'])
    pearson_corr = round(pearson_corr, 2)
else:
    pearson_corr = None

pearson_corr
