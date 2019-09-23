import csv
from .base import BaseParser
import os


class ParseWordsSeries(BaseParser):
    name_series = None

    def scan_all_files(self, num_series):
        print(self.name_folder)
        print(num_series)
        files = os.listdir(self.name_folder)
        files.sort()
        self.name_series = files[int(num_series)-1]
        path_file = f"{self.name_folder}/{self.name_series}"
        self.add_lines_from_file(path_file)
        self.list_line = [x for x in self.list_line if x.strip() != '']
        # self.list_line = [x.lower() for x in self.list_line]

        wet_list_line = self.list_line
        self.to_dry_list_line(wet_list_line)
        self.words = [self.delete_symbols(x) for x in self.words]
        self.words = [x.lower() for x in self.words]
        self.set_words = set(self.words)
        self.count_words()
        self.check_in_vacabulary_active()

    def write_file_csv(self):
        destination = f"csv_{self.name_folder}/"
        if not os.path.exists(destination):
            os.makedirs(destination)
        with open(f"csv_{self.name_folder}/{self.name_series}.csv", 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(('word', 'word count'))
            for key, val in self.sort_words.items():
                writer.writerow((key, val))
