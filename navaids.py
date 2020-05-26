import argparse
import sys
import gzip
import shutil

from pathlib import Path

__author__ = 'Sebastian Heil'
__copyright__ = 'Copyright 2020, Sebastian Heil'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Sebastian Heil <https://github.com/heseba>'
__status__ = 'Dev'

__project_name__ = 'NavDataPro2FlightGear'
__description__ = 'Copies NavDataPro X-Plane 10 Nav Files (Navaids, Fixes, Airways) to FlightGear.'

NDPXPLANE10_NAVAID_DIR = Path('Custom data')
FG_NAVAID_DIR = Path('Navaids')

NDPXPLANE10_TO_FG_MAP = [
    (Path('earth_awy.dat'), Path('awy.dat')),
    (Path('earth_fix.dat'), Path('fix.dat')),
    (Path('earth_nav.dat'), Path('nav.dat')),
]

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description=__description__)
    arg_parser.add_argument('ndp_path', metavar='XP10_PATH', type=Path,
                            help='X-Plane 10 NavDataPro directory in which to look for Navaids, Fixes and Airways')
    arg_parser.add_argument('fg_data_path', metavar='FG_DATA', type=Path,
                            help='FlightGear data directory ($FG_ROOT) to which Navaids, Fixes and Airways will be copied')
    arg_parser.add_argument('--version', action='version', version=f'{__project_name__} navaids.py {__version__}\n{__copyright__}')

    args = arg_parser.parse_args()

    ndp_path = args.ndp_path
    fg_data_path = args.fg_data_path

    if not ndp_path.is_dir():
        sys.exit(f'Aborting: {ndp_path} is not a directory')

    if not fg_data_path.is_dir():
        sys.exit(f'Aborting: {fg_data_path} is not a directory')

    if not (fg_data_path / FG_NAVAID_DIR).is_dir():
        sys.exit(f'Aborting: FlightGear Navaids directory ({fg_data_path / FG_NAVAID_DIR}) not found')

    for file_pair in NDPXPLANE10_TO_FG_MAP:
        if not (ndp_path / NDPXPLANE10_NAVAID_DIR / file_pair[0]).exists():
            sys.exit(f'Aborting: {str(ndp_path / NDPXPLANE10_NAVAID_DIR / file_pair[0])} not found')

        (ndp_path / NDPXPLANE10_NAVAID_DIR / file_pair[0]).replace(ndp_path / NDPXPLANE10_NAVAID_DIR / file_pair[1])

        with open(ndp_path / NDPXPLANE10_NAVAID_DIR / file_pair[1], 'rb') as f_in:
            gz_archive = Path(str(ndp_path / NDPXPLANE10_NAVAID_DIR / file_pair[1]) + '.gz')
            with gzip.open(gz_archive, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        (ndp_path / NDPXPLANE10_NAVAID_DIR / file_pair[1]).replace(ndp_path / NDPXPLANE10_NAVAID_DIR / file_pair[0])

        gz_archive.replace(fg_data_path / FG_NAVAID_DIR / gz_archive.name)
