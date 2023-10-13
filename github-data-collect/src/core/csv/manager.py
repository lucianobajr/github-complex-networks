import csv

class ManagerCSV:
    def __init__(self, filename, header):
        self.filename = filename
        self.header = header

    def open_file(self, mode):
        return open(self.filename, mode, newline='', encoding='utf-8')

    def write_header(self):
        with self.open_file('w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.header)

    def write_data(self, data):
        with self.open_file('a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)