import argparse

parser = argparse.ArgumentParser(description='Print selected parts of lines from each FILE to standard output.')
parser.add_argument('file', type=str,
                    help='an file for the action')
parser.add_argument('integer', type=int, help='an integer for the action')      
parser.add_argument('-c','--characters', action='store_true',
                    help='select only these characters')
parser.add_argument('-f','--fields', action='store_true',
                    help='select only these fields;  also print any line that contains no delimiter character')
args = parser.parse_args()

if args.characters:
    files = open(args.file, 'r')
    lines = files.readlines()
    files.close()
    for line in lines:
        line = line.strip()
        print(line[args.integer])
elif args.fields:
    files = open(args.file, 'r')
    lines = files.readlines()
    files.close()
    for line in lines:
        line = line.strip()
        line1 = line.split('\t')
        print(line1[args.integer - 1 ])
else:
    print('cut: you must specify a list of bytes, characters, or fields\n'+
"Try 'cut --help' for more information.")