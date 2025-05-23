import pandas as pd

# Mostra tutte le colonne
pd.set_option('display.max_columns', None)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    print("[transform] Inizio trasformazione...")

    # 1. Normalizza nomi colonne
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # 2. Pulisce i nomi propri (maiuscole)
    df['name'] = df['name'].str.title()

    # 3. Conversione date
    df['date_of_admission'] = pd.to_datetime(df['date_of_admission'], errors='coerce')
    df['discharge_date'] = pd.to_datetime(df['discharge_date'], errors='coerce')

    # 4. Calcolo durata ricovero
    df['hospital_stay_days'] = (df['discharge_date'] - df['date_of_admission']).dt.days

    # 5. Pulisce e normalizza campi stringa
    str_cols = ['gender', 'blood_type', 'medical_condition', 'doctor', 'hospital',
                'insurance_provider', 'admission_type', 'medication', 'test_results']
    for col in str_cols:
        df[col] = df[col].str.strip().str.title()

    # 6. Billing amount in float
    df['billing_amount'] = pd.to_numeric(df['billing_amount'], errors='coerce')

    # 7. Room number in intero
    df['room_number'] = pd.to_numeric(df['room_number'], errors='coerce', downcast='integer')

    # 8. Rimuovi righe con troppe info mancanti
    df.dropna(subset=['date_of_admission', 'discharge_date', 'billing_amount'], inplace=True)

    # 9. Gruppi di età
    def age_group(age):
        if age < 18:
            return "Child"
        elif age < 40:
            return "Young Adult"
        elif age < 65:
            return "Adult"
        else:
            return "Senior"
    df['age_group'] = df['age'].apply(age_group)

    # 10. Raggruppamento condizioni mediche (solo le top 5, il resto in "Other")
    top_conditions = df['medical_condition'].value_counts().nlargest(5).index
    df['condition_group'] = df['medical_condition'].apply(lambda x: x if x in top_conditions else "Other")

    # 11. Flag per ricovero lungo
    df['long_stay'] = df['hospital_stay_days'] > 10

    # 12. Mese di ammissione (nome del mese invece di numero)
    df['admission_month'] = df['date_of_admission'].dt.strftime('%B')

    # 13. Costo giornaliero stimato
    df['daily_cost_estimate'] = df['billing_amount'] / df['hospital_stay_days']
    df['daily_cost_estimate'] = df['daily_cost_estimate'].replace([float('inf'), float('nan')], 0)


    print("[transform] Trasformazione completata. Nuovo shape:", df.shape)
    return df
