import os
import sys
from glob import glob
from CompilationEngine import CompilationEngine
from JackTokenizer import JackTokenizer, TokenType, KeyWord

input = sys.argv[1]

if os.path.isdir(input):
    input_files = glob(input + '/*.jack')
else:
    input_files = [input]

for input_file in input_files:
    print("Processing file ", input_file)
    output_file = input_file.replace('.jack', '.vm')
    CompilationEngine(input_file, output_file)
