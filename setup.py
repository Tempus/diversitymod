import os, sys, shutil
from cx_Freeze import setup, Executable

#build_exe_options = {"packages": ["os"], 'include_files': ['diversitymod files/']}
#base = None
versionNum = '1.00'
installName = 'DiversityMod-' + versionNum

#if sys.platform == "win32":
#	base = "Win32GUI"
installDir = 'target/' + installName + '/'
	
#setup( name = "guifoo",
#		version = versionNum,
#		description = 'DiversityMod-' + versionNum,
#		options = {"build_exe": build_exe_options},
#		executables = [Executable("diversi.ymod.py", base=base)])


shutil.copytree('dist/', installDir)

shutil.copytree('diversitymod files/', installDir + 'diversitymod files/')

#shutil.copy('extra_files', installDir)
shutil.copy('README.md', installDir+"/README.txt")
shutil.copy('options.ini', installDir+"/options.ini")

#with open(installDir + "version.txt", 'w') as f:
#  f.write(version)
shutil.make_archive("target/" + installName, "zip", 'target', installName + "/")