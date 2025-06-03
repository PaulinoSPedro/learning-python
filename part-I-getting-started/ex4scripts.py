#!python3.7
#!/usr/local/bin/python
import sys
print(sys.version.split()[0])

''' 
The first line designate either the directory path to the desired program itself, or an invocation of env Unix utility that looks up the target per your PATH setting.

This is useful to set the Python version on which the program will run.

Type "chmod +x ex4scripts.py" to make it executable

You can use the following to select versions with Unix-style top-of-script comments:

#!python[version]
#!python2
#!python3.7
#!/usr/bin/python2.7
#!/usr/bin/env python3

With command use the following forms:

py -2 ex4scripts.py
py -2.7 ex4scripts.py
py -3.13 ex4scripts.py

Using commands you can overrite Unix-Style #! defined on file.
'''