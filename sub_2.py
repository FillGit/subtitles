import os
from sys import argv
from sub_2.base import ParserSub2

def write_file(decrease_lines, name_file, percent):
    destination = 'subtitles_res'
    if not os.path.exists(destination):
        os.makedirs(destination)
    f = open(f"{destination}/{name_file}--{percent}per.sub", 'w')
    for index in decrease_lines:
        f.write(index)
    f.close()

name_sub_series = argv[1]
percent = argv[2]

print(argv[1], argv[2])

pars = ParserSub2(name_folder='subtitles_org')
pars.scan_all_files(name_sub_series)
pars.decrease_lines(percent)

write_file(pars.decrease_lines(percent), name_sub_series, percent)



