from pathlib import Path
from io import StringIO
from csv import reader
import numpy as np

#** Method: Using csv
def readfile(input: Path):
    with open(input) as file:
        content = file.read()
    processed = content.replace('   ', '\t')
    listfile = reader(StringIO(processed), delimiter='\t',)
    return listfile

def load_input(input: Path, load_type: str = 'day1') -> np.array:
    #! load_type need change to delimiter, but this works for now
    intarr = np.loadtxt(input, delimiter=' ',  dtype=int, usecols= (0, 3))
    return intarr


#*-Old/Test----------
# file_inp = 'input.txt'
# file_in = Path(file_inp)
# contents = loadfile_np(file_in)
#-----
# input_text = file_in.read_text()
# print(input_text)
# input_list = reader(file_inp)

# for i in input_list:
#    print(i)