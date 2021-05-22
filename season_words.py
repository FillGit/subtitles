from sys import argv
from parser.season import ParseWordsSeason


name_folder = argv[1]

pars = ParseWordsSeason(name_folder=name_folder)
pars.scan_all_files()
print(len(pars.set_words))

pars.write_file_csv()
