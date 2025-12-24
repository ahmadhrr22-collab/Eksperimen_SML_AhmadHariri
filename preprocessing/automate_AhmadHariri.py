import pandas as pd
import os

# 1. Load Data
path_raw = 'dataset_raw/dataset_bank.csv' 
if not os.path.exists(path_raw):
    
    path_raw = '../dataset_raw/dataset_bank.csv'

df = pd.read_csv(path_raw, sep=';') 
df_clean = df.dropna()

# 3. Save Data
output_filename = 'preprocessing/preprocessed_data.csv'
df_clean.to_csv(output_filename, index=False)

print(f"Sukses! Data telah diproses dan disimpan ke {output_filename}")