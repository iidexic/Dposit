from pathlib import Path, WindowsPath, PosixPath
from iteration_utilities import first
import sqlite3

def getType(pathlist, ftype):
    return {x for x in pathlist.iterdir() if x.suffix == ftype}

def getfiles_folder(dir: str | Path, filetypes: str | set = {"all_types"}) -> set[Path]:
    if isinstance(dir,Path):
        f = dir.iterdir()
    else:
        f = Path(dir).iterdir()

    if isinstance(filetypes,str):
        return {x for x in f if x.suffix == filetypes}
    if first(filetypes) == 'all_types':
        return {x for x in f if x.is_file()}
    return {x for x in f if x.suffix in filetypes}

def getfiles_deep(dir: str | Path, filetypes: str | set = "all_types", maxdepth: int = 2) -> set[Path]:
    if maxdepth>0:
        pass
    pass