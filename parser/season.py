import csv
from .base import BaseParser
import os


class ParseWordsSeason(BaseParser):
    def write_file_csv(self):
        destination = f"csv_{self.name_folder}/"
        if not os.path.exists(destination):
            os.makedirs(destination)
        with open(f"csv_{self.name_folder}/{self.name_folder}.csv", 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(('word', 'word count'))
            for key, val in self.sort_words.items():
                writer.writerow((key, val))
