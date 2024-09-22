import re
import csv

log_file_path = 'mapper_fixed.log'
csv_file_path = 'RunTimeError_SMILES_rxnmapper.csv'

pattern = re.compile(r': (.*?);')

extracted_texts = []

with open(log_file_path, 'r') as log_file:
    for line in log_file:
        match = pattern.search(line)
        if match:
            extracted_text = match.group(1)
            extracted_texts.append([extracted_text])

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['SMILES'])
    writer.writerows(extracted_texts)

print(f'Textos extraídos foram salvos em {csv_file_path}')
