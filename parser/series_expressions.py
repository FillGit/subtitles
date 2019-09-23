import csv
from .base import BaseParser
import os


class SeriesExpressions(BaseParser):
    def __init__(self, **kwargs):
        self.words = []
        self.list_line = []
        self.all_expressions = []
        self.regular_expressions = {}
        self.list_join = self._create_list_join()
        self.season = kwargs['season']
        series = kwargs['series']
        files = os.listdir(self.season)
        files.sort()
        self.name_file = files[int(series)-1]
        self.path_file = f"{self.season}/{self.name_file}"

    def _find_regular_expression(self, expression, len_list):
        list_join = ' '.join([word for word in self.list_join])
        count_expressions = list_join.count(expression, 0, len_list)
        if count_expressions > 1:
            self.regular_expressions[expression] = count_expressions

    def _create_regular_expressions(self, len_list, word_count):
        i = 0
        len_whole_list = len(self.words)//word_count
        for word in self.words:
            if i > (len_whole_list - word_count):
                break
            expression = ' '.join([word for word in self.words[i:i+word_count]])
            self._find_regular_expression(expression, len_list)
            i = i + 1

    def scan_file(self):
        self.add_lines_from_file(self.path_file)
        self.list_line = [x for x in self.list_line if x.strip() != '']
        wet_list_line = self.list_line
        self.to_dry_list_line(wet_list_line)
        self.words = [self.delete_symbols(x) for x in self.words]

    def scan_series(self):
        self.scan_file()
        self.words = [x.lower() for x in self.words]
        len_list = len(self.list_join)
        self._create_regular_expressions(len_list, 3)
        self._create_regular_expressions(len_list, 4)
        self._create_regular_expressions(len_list, 5)
        # print(self.regular_expressions)

    def write_file_csv(self):
        destination = f'csv_{self.season}'
        if not os.path.exists(destination):
            os.makedirs(destination)
        with open(f"{destination}/exp_{self.name_file}", 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(('expression', 'expression_count'))
            for key, val in self.regular_expressions.items():
                writer.writerow((key, val))

    def _create_list_join(self):
        with open("all_expressions.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            list_join = []
            for line in reader:
                list_join.append(line['expression'])
            return list_join
