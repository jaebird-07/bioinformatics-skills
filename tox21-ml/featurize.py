from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski
import pandas as pd
df = pd.read_csv('tox21_raw.csv')

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve, roc_auc_score


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

features_df = pd.DataFrame(records)
print(features_df)

X = features_df.drop(columns=["mol_id", "SR-p53"])
y = features_df["SR-p53"]

print(X.shape) 
print(y.shape) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(X_train.shape, X_test.shape)
print(y_train.mean(), y_test.mean())

model = LogisticRegression()
model.fit(X_train, y_train)

print(model.coef_)
print(model.intercept_)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model.fit(X_train_scaled, y_train)
print(model.coef_)
print(model.intercept_)

y_pred = model.predict(X_test_scaled)
accuracy_score(y_test, y_pred)

print(y_pred.sum())

print(y_test.sum())
len(X_test_scaled) 

correct = ((y_pred == 1) & (y_test == 1)).sum()
print(correct)


model_balanced = LogisticRegression(class_weight='balanced')
model_balanced.fit(X_train_scaled, y_train)

y_pred_balanced = model_balanced.predict(X_test_scaled)
print(y_pred_balanced.sum())
print(accuracy_score(y_test, y_pred_balanced))

correctly_caught = ((y_pred_balanced == 1) & (y_test == 1)).sum()
print(correctly_caught)

y_scores_both = model.predict_proba(X_test_scaled)
y_scores = model.predict_proba(X_test_scaled)[:, 1]
print(y_scores)

TP = ((y_pred_thresh == 1) & (y_test == 1)).sum()
FP = ((y_pred_thresh == 1) & (y_test == 0)).sum()
TN = ((y_pred_thresh == 0) & (y_test == 0)).sum()
FN = ((y_pred_thresh == 0) & (y_test == 1)).sum()

TPR = TP / (TP + FN)
FPR = FP / (FP + TN)

fpr, tpr, thresholds = roc_curve(y_test, y_scores)
auc = roc_auc_score(y_test, y_scores)
print(fpr, tpr, thresholds)
print(auc)