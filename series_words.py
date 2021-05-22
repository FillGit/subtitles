from sys import argv
from parser.series import ParseWordsSeries


name_folder = argv[1]
num_series = argv[2]

pars = ParseWordsSeries(name_folder=name_folder)
pars.scan_all_files(num_series)
print(len(pars.set_words))

pars.write_file_csv()
