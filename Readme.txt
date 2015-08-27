==============Requirments=============
Python 2.7 : http://www.python.org/download/
Python for .Net (included) : http://pythonnet.sourceforge.net/
py2exe : http://www.py2exe.org/

==============included files==========
COConverter.py
ViewReaders.py
Logger.py
python.exe
Python.Runtime.dll
CruiseDAL.dll
System.Data.SQLite.dll
Mk4py.pyd
clr.pyd
setup.py
build.bat
RunCOConvert.bat

.project
.pydevproject


==============Build===============
Assuming Python 2.7 is installed and py2exe is installed 
run Build.bat 
The script will copy CruiseDAL.dll from ..\..\CruiseDAL\Trunk\CruiseDAL_FF35\bin\x86\Release\
the output will be in the dist sub-folder



==============Running CO Converter====
Method 1:
	use CSM by opening a .crz file with File > Open
	
Method 2:
	Drag a .crz file onto RunCOConverter.bat


==============Develpoment Notes=======
To modify COConverter as a project in Eclipse using the PyDev
 plugin use the .project file located in this folder
 
 
 See http://pydev.org/ 
 