from distutils.core import setup
import py2exe
from glob import glob

data_files = [(".\Microsoft.VC90.CRT", glob(r'C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*')), '.\Python.Runtime.dll', '.\System.Data.SQLite.dll', '.\CruiseDAL.dll', '.\RunCOConvert.bat']

setup(
    data_files=data_files,
	console=['COConverter.py']
  )