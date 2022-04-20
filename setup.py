from distutils.command.build import build
from msilib import Win64
from xml.etree.ElementInclude import include
from cx_Freeze import setup, Executable
base = Win64
executables= [executable("contact.py", base=base)]
buildOption= dict(
    includes=["tkinter"]
)
setup(
    name="PyRepertoire",
    version="1.0",
    description= "repertoire fait a partir de dictionaire pour un exercice",
    author= "Nathan A",
    options=dict(build_exe=buildOption),
    executables = executables
)

