from sys import argv
from parser.regular_expressions import RegularExpressions


seasons = argv[1:]

pars = RegularExpressions()
pars.scan_all_seasons(seasons=seasons)

pars.write_file_csv()
