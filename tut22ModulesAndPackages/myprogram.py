# modules are just .py scripts that you call in another .py script
# Packages are collection of modules

# When running this program, make sure you navigate to right directory
from mymodule import my_func

my_func()

######

#from mainpackage import scriptinmainpackage

#from mainpackage.subpackage import scriptinsubpackage

#scriptinmainpackage.main_report()

#scriptinsubpackage.sub_report()

##############

# If you call the function then we don't need mention the package name while calling

from mainpackage.scriptinmainpackage import main_report

from mainpackage.subpackage.scriptinsubpackage import sub_report

main_report()

sub_report()



