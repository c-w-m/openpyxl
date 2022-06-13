# The script assumes that the virutalenvironments have been created for a project using tox.

import subprocess
import sys

envs = ['py27', 'py35', 'py36', 'py37',]

passthrough = sys.argv[1:] or []

for e in envs:
    subprocess.run([".tox/{0}/bin/pip".format(e), "-q", "install", "-e", "."])
    subprocess.run([".tox/{0}/bin/pip".format(e), "-q", "install", "-U", "xlsxwriter", "lxml"])
    subprocess.run([".tox/{0}/bin/python".format(e), "benchmark.py"] + passthrough)