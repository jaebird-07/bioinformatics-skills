from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski
import pandas as pd
df = pd.read_csv('tox21_raw.csv')

def get_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    result = {}
    result["MW"] = Descriptors.ExactMolWt(mol)
    result["Lipophilicity"] = Descriptors.MolLogP(mol)
    result["Polar SA"] = Descriptors.TPSA(mol)
    result["HDonors"] = Lipinski.NumHDonors(mol)
    result["HAcceptors"] = Lipinski.NumHAcceptors(mol)
    result["Rotatable bonds"] = Lipinski.NumRotatableBonds(mol)
    result["Aromatics"] = Lipinski.NumAromaticRings(mol)
    return result
print(get_descriptors("CCOc1ccc2nc(S(N)(=O)=O)sc2c1"))


tested_df = df[df["SR-p53"].notna()][['SR-p53', 'mol_id', 'smiles']]
print(tested_df)
print(len(tested_df))

records = []

for _, row in tested_df.iterrows():
    descriptors = get_descriptors(row["smiles"])
    if descriptors is None:
        continue
    descriptors["mol_id"] = row["mol_id"]
    descriptors["SR-p53"] = row["SR-p53"]
    records.append(descriptors)

print(len(records))
print(records[0])