"""
pyzz - A tool belt for the shell.
Usage:
    pyzz
    pyzz add <function>
    pyzz functions
    pyzz --help
Options:
    add <function>    Add a new function <function>.
    functions         Show all available functions.
    --help            Show this screen.
"""
from __future__ import print_function
from docopt import docopt
import os
from os.path import isdir, isfile, dirname, abspath

def show_functions(args):
    cwd = dirname(abspath(__file__))
    files = os.listdir(cwd)
    functions = [file for file in files \
                    if isdir(cwd + '/' + file) and not file.startswith('__')]
    return "\r\n".join(functions)

def add_function(args):
    pyzz_dir = os.getcwd() + '/pyzz/'
    template_path = pyzz_dir + 'init.py.template'
    if isdir(pyzz_dir) and isfile(template_path):

        function_path = pyzz_dir + args['<function>']
        os.mkdir(function_path)

        with open(template_path, 'r') as template:
            template_content = ''.join(template.readlines())

        with open(function_path + '/__init__.py', 'w') as pyfile:
            pyfile.write(template_content.format(args['<function>']))

        return "Function added succesfully. Have fun building it!"

    else:
        return 'Error: Could not find pyzz package and template init file. ' \
                'Am i inside pyzz project folder?'

def pyzz():
    return "pyzz - A tool belt for the shell."

def main():
    args = docopt(__doc__)
    if args['functions']:
        print(show_functions(args))
    else:
        if args['add']:
            print(add_function(args))
        else:
            print(pyzz())
