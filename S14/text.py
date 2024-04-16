from pathlib import Path

if len(Path('idex.html').read_text()) > 0:
    print('ok')
else:
    print('no')