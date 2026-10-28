import pandas as pd

file_path = (
    r"C:\Users\Musa\fastapi-jwt-fashion-api\data\vellamo_fashion_sales_fy2025_with_lookups.xlsx"
)

df = pd.read_excel(file_path)


def get_sales():

    return df.head(20).to_dict(
        orient="records"
    )

def get_summary():

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns)
    }