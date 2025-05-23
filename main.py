import os
from etl.extract import extract
from etl.transform import transform
from etl.load import load

def main():
    csv_path = os.getenv("CSV_PATH", "data/healthcare_dataset.csv")
    db_url = os.getenv("DB_URL", "postgresql+psycopg2://etl_user:etl_pass@localhost:5432/etl_db")
    table_name = "healthcare_data"

    print("[main] Estrazione dati...")
    df = extract(csv_path)

    if df is None:
        print("[main] Estrazione fallita. Interruzione processo.")
        return

    print("[main] Trasformazione dati...")
    df_clean = transform(df)

    print("[main] Caricamento dati nel DB...")
    load(df_clean, table_name, db_url)

    print("[main] Processo ETL completato.")

if __name__ == "__main__":
    main()
