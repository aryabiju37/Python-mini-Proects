from packages import mymainscript
from packages.subpackage import mysubscript


print("I am inside modules folder calling packages and subpackages directory/packages-> with __init__.py files ")
print("**************************************************************************************************************")
mymainscript.report_main()
mysubscript.report_sub()