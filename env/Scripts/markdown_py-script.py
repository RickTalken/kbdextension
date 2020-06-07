#!C:\PythonProjects\kbdextension\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Markdown','console_scripts','markdown_py'
__requires__ = "Markdown"
import re
import sys
from pkg_resources import load_entry_point

if __name__ == "__main__":
    sys.argv[0] = re.sub(r"(-script\.pyw?|\.exe)?$", "", sys.argv[0])
    sys.exit(load_entry_point("Markdown", "console_scripts", "markdown_py")())
