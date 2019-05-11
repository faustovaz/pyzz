from setuptools import setup

setup(
    name='pyzz',
    install_requires = ['docopt', 'pytest'],
    entry_points = {
        'console_scripts' : [
            'pyzz = pyzz.__init__:main'
        ]
    },
)
