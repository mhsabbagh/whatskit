from distutils.core import setup
from subprocess import call
from glob import glob
from os.path import splitext, split

data_files = [ ("share/whatskit", ["ui/ui.glade"]),
                    ("share/pixmaps", ["data/whatskit.png"]),
                     ("share/applications", ["data/whatskit.desktop"]) ] 

setup(name = "whatskit",
      version = "0.1",
      description = "A standalone desktop window for web.whatsapp.com.",
      author = "M.Hanny Sabbagh", 
      author_email = "mhsabbagh@outlook.com",
      url = "https://github.com/mhsabbagh/whatskit",
      license='GPLv3',
      scripts=['whatskit'],
      data_files=data_files)

