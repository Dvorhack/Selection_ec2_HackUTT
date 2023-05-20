from pathlib import Path
import subprocess

pathlist = Path('./').glob('*/*')
for path in pathlist:
     # because path is object not string
     path_in_str = str(path)
     if path_in_str.startswith('.git'):
        continue
     subprocess.Popen(f'touch {path_in_str}/.gitkeep'.split())
