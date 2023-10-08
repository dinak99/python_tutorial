import platform
import platform as pl
from platform import release

sysName = pl.system()
print(sysName)

rls = release()
print(rls)

resources = dir(platform)
print(resources)  # list all the function names (or variable names)
