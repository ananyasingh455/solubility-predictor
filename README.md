# Molecular Solubility Predictor

This project uses Machine Learning (Random Forest) and the **RDKit** cheminformatics library to predict the aqueous solubility ($LogS$) of small organic molecules based on their SMILES strings.

## Overview
The model is trained on the **Delaney (ESOL) Dataset**. It extracts four key molecular descriptors:
1. **MolLogP**: Octanol-water partition coefficient.
2. **MolWt**: Molecular Weight.
3. **NumRotatableBonds**: Flexibility of the molecule.
4. **Aromatic Proportion**: Ratio of aromatic atoms to heavy atoms.
