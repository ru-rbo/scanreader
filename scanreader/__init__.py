from .core import read_scan

if __name__ == "__main__":
    from pathlib import Path
    file = [x for x in Path('/data2/fpo/data/').glob("*.tif*")][0]

