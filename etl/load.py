import pandas as pd
from sqlalchemy import create_engine

def load(df: pd.DataFrame, table_name: str, db_url: str):
    print("[load] Inizio caricamento dati su PostgreSQL...")

    engine = create_engine(db_url)

    try:
        # Carica il dataframe nella tabella, sovrascrivendo se esiste
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"[load] Caricamento completato. {len(df)} righe caricate nella tabella '{table_name}'.")
    except Exception as e:
        print(f"[load] Errore durante il caricamento: {e}")
