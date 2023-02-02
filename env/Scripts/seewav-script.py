#!"c:\users\smart\documents\youtube automator\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'seewav==0.1.0','console_scripts','seewav'
__requires__ = 'seewav==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('seewav==0.1.0', 'console_scripts', 'seewav')()
    )
