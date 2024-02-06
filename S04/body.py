from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "Sequences/U5.fa"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

header = file_contents.split('\n')

for n in range(1, len(header)):
    print(header[n])
