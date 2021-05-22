from sys import argv
from parser.series_expressions import SeriesExpressions


season = argv[1]
series = argv[2]

pars = SeriesExpressions(season=season, series=series)
pars.scan_series()

pars.write_file_csv()
