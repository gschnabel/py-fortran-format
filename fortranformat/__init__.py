__version__ = '0.1.9'

import sys
IS_PYTHON3 = sys.version_info[0] >= 3

if IS_PYTHON3:
    exec('from .FortranRecordReader import FortranRecordReader')
    exec('from .FortranRecordWriter import FortranRecordWriter')
    exec('from . import config')
else:
    exec('from FortranRecordReader import FortranRecordReader')
    exec('from FortranRecordWriter import FortranRecordWriter')
    exec('import config')


