import os, sys, shutil, py2exe
from distutils.core import setup

#Here is where you can set the name for the release zip file and for the install dir inside it.
version = "0.4"
installName = 'DiversityMod-' + version

#target is where we assemble our final install. dist is where py2exe produces exes and their dependencies
if os.path.isdir('target/'):
  shutil.rmtree('target/')
installDir = 'target/' + installName + '/'

#then build the option builder using normal py2exe
sys.argv.append('py2exe')
#setup(console=['diversitymod.py','RemoveAllRebirthMods.py'])
setup(
	console=['diversitymod.py','RemoveAllRebirthMods.py'],
	options = {
		'py2exe': {
			'includes': ['shutil','random','PIL','os','_winreg'],
			'bundle_files':2
		}
	}
)

shutil.copytree('dist/', installDir)

shutil.copytree('diversitymod files/', installDir + 'diversitymod files/')

#shutil.copy('extra_files', installDir)
shutil.copy('README.md', installDir)

with open(installDir + "version.txt", 'w') as f:
  f.write(version)
shutil.make_archive("target/" + installName, "zip", 'target', installName + "/")