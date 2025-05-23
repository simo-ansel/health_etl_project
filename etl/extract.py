import pandas as pd

def extract(csv_path):
    """
    Estrae il dataset dal file CSV.

    Args:
        csv_path (str): percorso del file CSV.

    Returns:
        pd.DataFrame: dati estratti.
    """
    try:
        print('ciaoo')
        print('daje')
        df = pd.read_csv(csv_path)
        print(f"[extract] Dataset caricato con successo: {df.shape[0]} righe, {df.shape[1]} colonne.")
        return df
    except FileNotFoundError:
        print(f"[extract] ERRORE: file non trovato nel percorso: {csv_path}")
        return None
    except Exception as e:
        print(f"[extract] ERRORE generico: {e}")
        return None
