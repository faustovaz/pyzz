from setuptools import setup
from os import listdir
from os.path import dirname, abspath, isdir, isfile

def scripts():
    scripts = ['pyzz = pyzz.__init__:main']
    pyzz_path = dirname(abspath(__file__)) + '/pyzz/'
    for file in listdir(pyzz_path):
        full_file_path = pyzz_path + file
        if isdir(full_file_path) and isfile(full_file_path + '/__init__.py'):
            scripts.append('{0} = pyzz.{0}.__init__:main'.format(file))
    return scripts

setup(
    name='pyzz',
    install_requires = ['docopt', 'pytest'],
    entry_points = {
        'console_scripts' : scripts()
    },
)
