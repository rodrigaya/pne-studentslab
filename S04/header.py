from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "Sequences/RNU6_269P.fa"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

header = file_contents.split('\n')

print('First line of the ' + FILENAME + ' file:\n' + header[0])
