import argparse
import re
import sys

from pathlib import Path

__author__ = 'Sebastian Heil'
__copyright__ = 'Copyright 2020, Sebastian Heil'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Sebastian Heil <https://github.com/heseba>'
__status__ = 'Dev'

__project_name__ = 'NavDataPro2FlightGear'
__description__ = 'Renames NavDataPro Level-D Navdata Files to work with extract-navdata.py.'

SUBDIRECTORY = 'navdata'
CYCLE_INFO = 'cycle_info.txt'
PROCEDURE_FILE_PATTERN = re.compile(r'(?P<icao>[A-Z0-9]{4})\.xml')

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description=__description__)
    arg_parser.add_argument('path', metavar='LD_PATH', type=Path,
                            help='Level-D 767 NavDataPro directory in which to rename files')

    arg_parser.add_argument('--version', action='version', version=f'{__project_name__} rename_procedures.py {__version__}\n{__copyright__}')

    args = arg_parser.parse_args()
    navdata_path = args.path

    if not navdata_path.exists() or not navdata_path.is_dir():
        sys.exit(f'Aborting: Cannot find {navdata_path} directory')

    if not (navdata_path / CYCLE_INFO).exists() and (navdata_path / SUBDIRECTORY / CYCLE_INFO).exists():
        navdata_path = navdata_path / SUBDIRECTORY

    if not (navdata_path / CYCLE_INFO).exists():
        sys.exit(f'Aborting: Cannot find {CYCLE_INFO} in {navdata_path}')

    for file in navdata_path.iterdir():
        if file.is_file():
            match = PROCEDURE_FILE_PATTERN.match(file.name)

            if match:
                icao = match.group('icao')
                file.rename(navdata_path / f'{icao}.procedures.xml')
