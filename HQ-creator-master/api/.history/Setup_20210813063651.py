from cx_Freeze import setup, Executable

base = None    

executables = [Executable("myfirstprog.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages': ["Conversor", ""],
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)