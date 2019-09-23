import csv
from .base import BaseParser
import os


class RegularExpressions(BaseParser):
    def __init__(self, **kwargs):
        self.words = []
        self.list_line = []
        self.regular_expressions = {}

    def _find_regular_expression(self, list_join, expression, len_list):
        count_expressions = list_join.count(expression, 0, len_list)
        if count_expressions > 1:
            self.regular_expressions[expression] = count_expressions

    def _create_regular_expressions(self, list_join, len_list, word_count):
        i = 0
        len_whole_list = len_list//word_count
        for word in self.words:
            if i > (len_whole_list - word_count):
                break
            expression = ' '.join([word for word in self.words[i:i+word_count]])
            self._find_regular_expression(list_join, expression, len_list)
            i = i + 1

    def scan_all_files(self, name_season):
        files = os.listdir(name_season)
        for file in files:
            path_file = f"{name_season}/{file}"
            self.add_lines_from_file(path_file)
        self.list_line = [x for x in self.list_line if x.strip() != '']
        wet_list_line = self.list_line
        self.to_dry_list_line(wet_list_line)
        self.words = [self.delete_symbols(x) for x in self.words]

    def scan_all_seasons(self, seasons):
        for season in seasons:
            self.scan_all_files(season)
        self.words = [x.lower() for x in self.words]
        len_list = len(self.words)
        list_join = ' '.join([word for word in self.words])
        self._create_regular_expressions(list_join, len_list, 3)
        self._create_regular_expressions(list_join, len_list, 4)
        self._create_regular_expressions(list_join, len_list, 5)
        # print(self.regular_expressions)

    def write_file_csv(self):
        destination = 'csv_regular_expressions'
        if not os.path.exists(destination):
            os.makedirs(destination)
        with open(f"{destination}/all_regular_expressions.csv", 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(('expression', 'expression_count'))
            for key, val in self.regular_expressions.items():
                writer.writerow((key, val))
