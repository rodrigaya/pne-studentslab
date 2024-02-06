from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "Sequences/ADA.fa"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

seq_list = file_contents.split('\n')

seq = ''
for n in range(1, len(seq_list)):
    seq += seq_list[n].replace('\n', '')

print(len(seq))