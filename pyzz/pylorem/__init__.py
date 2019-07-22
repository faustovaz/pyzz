"""
pylorem - Generate LoremIpsums on the fly
All messages are genereated using the LoremIpsum Api (https://loripsum.net)
Usage:
    pylorem
    pylorem -n <number-of-paragraphs>
    pylorem (-s| -m | -l | -v)
    pylorem (-s| -m | -l | -v) -n <number-of-paragraphs>
    pylorem -h | --help 
Options:
    -s                  Short size paragraphs
    -m                  Medium size paragraphs
    -l                  Long size paragraphs
    -v                  Very Long size paragraphs
    -n                  Genereate with a given number of paragraphs
    -h | --h            Shows this help message
"""

from __future__ import print_function
from docopt import docopt
import urllib.request as request

def main():
    url = 'https://loripsum.net/api/plaintext/'
    args = docopt(__doc__)
    
    if args['-s']:
        url = url + 'short/'
    elif args['-m']:
        url = url + 'medium/'
    elif args['-l']:
        url = url + 'long/'
    elif args['-v']:
        url = url + 'verylong/'

    if args['-n']:
        url = url + args['<number-of-paragraphs>'] + '/'

    response = request.urlopen(url)
    print(str(response.read().decode('utf-8')))


if __name__ == '__main__':
    main()
