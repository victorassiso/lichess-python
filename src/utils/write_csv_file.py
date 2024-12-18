import csv

def write_csv_file(file_path, data):
  with open(file_path, 'w', newline='') as file:
    fieldnames = data[0].keys() if data else []
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)