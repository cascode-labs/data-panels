"""
data-panels command line interface (CLI)
"""
import argparse, sys
from pathlib import Path
from data_panels.api import run
import data_panels as data_panels_module

def data_panels():
    parser = argparse.ArgumentParser("DataPanels")
    parser.add_argument('-d', '--dataset', type=_check_path, 
        help="a path to a Cadence dataset (history result) directory")
    parser.add_argument('-v', '--version', action="store_true",
        help="display the version number")
    args = parser.parse_args()
    if args.version:
        print("v" + data_panels_module.__version__)
        sys.exit()
    run(args.dataset)

def _check_path(path: str) -> str:
    if Path(path).is_dir() or Path(path).is_file():
        return path
    raise argparse.ArgumentError(None, f"Invalid Path: {path}")


if __name__ == '__main__':
    data_panels()
