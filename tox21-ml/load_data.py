import pandas as pd

df = pd.read_csv('tox21_raw.csv')

tested_active = df[df['SR-p53'] == 1]['mol_id']['smiles']
tested_inactive = df[df['SR-p53'] == 0]['mol_id']['smiles']
not_tested = df[df['SR-p53'].isna()]['mol_id']
print(tested_active, tested_inactive, not_tested )

print(len(tested_active))
print(len(tested_inactive))
print(len(not_tested))

active_percentage = len(tested_active) / (len(tested_active) + len(tested_inactive))
print(active_percentage)

col = df["SR-p53"]
tested = col.dropna()

int((tested==1).sum())
int((tested==0).sum())

active_frac = (tested==1).mean() * 100 
print(active_frac)