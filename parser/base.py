import os
import csv


class BaseParser(object):
    def __init__(self, **kwargs):
        self.name_folder = kwargs['name_folder']
        self.words = []
        self.list_line = []
        self.set_words = None
        self.sort_words = {}

    def add_lines_from_file(self, file):
        with open(file) as f:
            for line in f:
                self.list_line.append(line)

    def to_dry_list_line(self, wet_list_line):
        dry_list_line = []
        next_time_period = False
        for line in wet_list_line:
            if not next_time_period:
                try:
                    int(line)
                except ValueError:
                    dry_list_line.append(line)
                    self.separate_line(line)
                else:
                    next_time_period = True
            else:
                next_time_period = False
        self.list_line = dry_list_line

    def separate_line(self, line):
        words = line.split()
        for word in words:
            self.words.append(word)

    def count_words(self):
        count_words = {}
        for word in self.set_words:
            count_words[word] = self.words.count(word)
        for word in sorted(count_words.items(), key=lambda para: para[1],
                           reverse=True):
            self.sort_words[word[0]] = word[1]

    def delete_symbols(self, word):
        symbols = ['!', '@', '#', '$', '%', '?', ',', '.', '\n', '<i>', '</i>',
                   ':', '-', '"', '0000', '—', '<', '>']
        if word == '\ufeff1':
            word = ''
        for symbol in symbols:
            if symbol in word:
                word = word.replace(symbol, '')
        return word

    def check_in_vacabulary_active(self):
        with open("vocabulary_active.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for line in reader:
                if line['word'] in self.sort_words:
                    self.sort_words.pop(line['word'])

    def scan_all_files(self):
        print(self.name_folder)
        files = os.listdir(self.name_folder)
        for file in files:
            path_file = f"{self.name_folder}/{file}"
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
