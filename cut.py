import argparse
import re
import sys
import subprocess

parser = argparse.ArgumentParser(description='Cut command')
parser.add_argument('-b', '--byptes', type=str,
                    metavar='LIST', help="select only these bytes")
parser.add_argument('-c', '--characters', type=str,
                    metavar='LIST', help="select only these characters")
parser.add_argument('-d', '--delimiter', type=str, metavar='DELIM',
                    help="use DELIM instead of TAB for field delimiter")
parser.add_argument('-f', '--fields', type=str, metavar='LIST',
                    help="select only these fields; also print any line that contains no delimiter character, unless the -s option is specified")
parser.add_argument('-n', action='store_true',
                    help="with -b: don't split multibyte characters")
parser.add_argument('--complement', action='store_true',
                    help='complement the set of selected bytes, characters or fields')
parser.add_argument('-s', '--only-delimited', action='store_true',
                    help='do not print lines not containing delimiters')
parser.add_argument('--output-delimiter', type=str, metavar='STRING',
                    help='use STRING as the output delimiter the default is to use the input delimiter')
parser.add_argument('--version', action='store_true',
                    help="output version information and exit")
args = parser.parse_args()

args_2 = ['wsl']
args_3 = sys.argv
for cut in args_3:
    if len(re.findall('cut.py', cut)) > 0:
        args_2.append(cut.strip('.\\').strip('./').strip('.py'))
    else:
        args_2.append(cut)
print(subprocess.run(args_2, shell=True,
      stdout=subprocess.PIPE).stdout.decode('utf8'))
