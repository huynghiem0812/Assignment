import argparse
import magic

parser = argparse.ArgumentParser(description='Determine type of FILEs.')
parser.add_argument('file', type=str,
                    help='an file for the action')                 
parser.add_argument('-b','--brief', action='store_true',
                    help='display just file type in brief mode')
parser.add_argument('-i','--mime', action='store_true',
                    help='output MIME type strings')
parser.add_argument('-f', '--ffFILE', action='store_true',
                    help='read the filenames to be examined from FILE')
args = parser.parse_args()

if args.brief:
    print(magic.from_file(args.file))
elif args.mime:
    mime = magic.Magic(mime=True)
    print(mime.from_file(args.file))
elif args.ffFILE:
    file = open("test.txt", 'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        line = line.strip()
        print(line + ' : ' + magic.from_file(line))
else:
    print(magic.from_file(args.file))