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

from docopt import docopt

def show_functions(args):
    return "TODO - Show all functions"

def add_function(args):
    return "TODO - Create a new pyzz function"

def pyzz():
    return "pyzz - A tool belt for the shell."

def main():
    args = docopt(__doc__)
    if args['functions']:
        show_functions(args)
    else:
        if args['add']:
            add_function(args)
        else:
            pyzz()
