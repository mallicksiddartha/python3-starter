from cx_Freeze import setup, Executable

setup(name = 'searchDataInFile',
      version = '0.1',
      description = 'Search stuff, then put result in file, then parse stuff',
      executables = [Executable('cx_freeze_source.py')])
