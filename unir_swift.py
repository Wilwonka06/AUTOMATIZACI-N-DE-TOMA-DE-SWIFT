import pandas as pd
import os

FOLDER = "countries_excel"
OUTPUT_FILE = "SWIFT_ALL_COUNTRIES_FINAL.xlsx"

all_dfs = []

for file in os.listdir(FOLDER):
    if file.endswith(".xlsx"):
        path = os.path.join(FOLDER, file)
        df = pd.read_excel(path, dtype=str)
        all_dfs.append(df)

final_df = pd.concat(all_dfs, ignore_index=True)

final_df.to_excel(OUTPUT_FILE, index=False)

print(f"Excel final generado: {OUTPUT_FILE}")
print(f"Total registros: {len(final_df)}")
