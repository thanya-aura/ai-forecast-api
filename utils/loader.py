import pandas as pd
from io import BytesIO

def load_forecast_from_file(file_bytes: bytes, filename: str) -> pd.DataFrame:
    if filename.endswith(".csv"):
        return pd.read_csv(BytesIO(file_bytes))
    elif filename.endswith((".xlsx", ".xls")):
        return pd.read_excel(BytesIO(file_bytes))
    else:
        raise ValueError("Unsupported file format")