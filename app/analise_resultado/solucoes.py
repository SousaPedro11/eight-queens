import os
from pathlib import Path


def ler(name, method='r'):
    BASEDIR = Path(os.path.abspath(os.path.dirname(__name__)))
    with open(os.path.join(BASEDIR, name), method) as f:
        linhas = f.read().splitlines()
    return linhas
