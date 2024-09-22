import pandas as pd

error_smiles_df = pd.read_csv('RunTimeError_SMILES_rxnmapper.csv')

dataset = pd.read_csv('../../data_processing_retroformer_pipeline/data_processing_pipeline/res/ready_data_no_atom_mapped.csv')

i = 0

for index, row in error_smiles_df.iterrows():
    smiles = row['SMILES']
    for secondary_metabolism in dataset[dataset['REACTION-SMILES'] == smiles]['SECONDARY-METABOLISM']:
        if secondary_metabolism:
            i += 1

message = 'There are {} RunTimeError reaction SMILES that belong to secondary metabolism pathways between {}.'.format(i, len(error_smiles_df))

with open('RunTimeErrorSMILES.txt', 'w') as file:
    file.write(message)