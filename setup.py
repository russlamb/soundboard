import os
from cx_Freeze import setup, Executable
import sys

# this was going to be used for tk UI
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [

    Executable('main.py',icon="038 Ninetales.ico", targetName="soundboard.exe",base=base)
]

include_files =[
    "face.png",
    #TODO: fix these to use a generic location
    #TODO: make only for windows builds
    #os.path.join(PYTHON_INSTALL_DIR,r"DLLs/tcl86t.dll"),
    #os.path.join(PYTHON_INSTALL_DIR,r"DLLs/tk86t.dll"),
    #os.path.join(PYTHON_INSTALL_DIR,r"vcruntime140.dll"),
    "sound.mp3"
]
includes = []

packages = [
    "play_sound"
]

options = {
    'build_exe': {
        "include_msvcr":True,
        "include_files": include_files,
        "includes" :includes ,

        "packages" : packages
    }
}

setup( name = "soundboard",
       version="1.0",
       description = "make sounds",
       options = options,
       executables=executables
       )
