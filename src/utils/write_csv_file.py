import csv
import os

def write_csv_file(file_path, data):
  # Cria o diretório se ele não existir
  os.makedirs(os.path.dirname(file_path), exist_ok=True)

  with open(file_path, 'w', newline='') as file:
    fieldnames = data[0].keys() if data else []
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)