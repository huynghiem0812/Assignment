import argparse
import re
import sys
import subprocess

parser = argparse.ArgumentParser(description='File command', add_help=False)
parser.add_argument('--help', action='store_true',
                    help='display this help and exit')
parser.add_argument('-b', '--brief', type=str, nargs='*',
                    metavar='filename', help='do not prepend filenames to output lines')
parser.add_argument('-C', '--compile', action='store_true',
                    help='write a magic.mgc output file that contains a pre-parsed version of the magic file or directory.')
parser.add_argument('-c', '--checking-printout',
                    help='print the parsed form of the magic file. This is usually used in conjunction with the -m flag to debug a new magic file before installing it.')
parser.add_argument('-e', '--exclude', type=str, metavar='TEST',
                    help='exclude TEST from the list of the test to be performed for file. Valid test are: apptype, ascii, cdf, compress, elf, encoding, soft, tar, text, tokens')
parser.add_argument('-F', '--separator', type=str, metavar='STRING',
                    help="use string as a separator instead of ':'.")
parser.add_argument('-f', '--files-from', type=str, metavar='FILE',
                    help='read the filenames to be examined from FILE.')
parser.add_argument('-h', '--no-dereference', type=str, nargs='*', metavar='filename',
                    help="don't followed symlinks (default POSIXLY_CORRECT is not set) (default).")
parser.add_argument('-i', '--mime', type=str, nargs='*', metavar='filename',
                    help='output MIME type strings (--mine-type and --mine-encoding')
parser.add_argument('-mime-type', '--mime-encoding', type=str, nargs='*',
                    metavar='filename', help='like -i, but print only the specified element(s)')
parser.add_argument('-k', '--keep-going', type=str, nargs='*',
                    metavar='filename', help="don't stop at the first match")
parser.add_argument('-L', '--dereference', type=str, nargs='*', metavar='filename',
                    help="followed symlinks (default POSIXLY_CORRECT is set)")
parser.add_argument('-m', '--magic-file', type=str, metavar='LIST',
                    help="use LIST as a colon-seperated list of magic number files")
parser.add_argument('-N', '--no-pad', type=str, nargs='*',
                    metavar='filename', help="do not pad output")
parser.add_argument('-n', '--no-buffer', type=str, nargs='*',
                    metavar='filename', help="do not buffer output")
parser.add_argument('-p', '--preserve-date', type=str, nargs='*',
                    metavar='filename', help='preserve access time on files')
parser.add_argument('-r', '--raw', type=str, nargs='*', metavar='filename',
                    help="don't translate unprintable chars to \ooo")
parser.add_argument('-s', '--special-files', type=str, nargs='*', metavar='filename',
                    help="causes file to also read argument files which are block or character special files")
parser.add_argument('-v', '--version', action="store_true",
                    help="print the version of the program and exit.")
parser.add_argument('-z', '--uncompress', type=str, nargs='*',
                    metavar='filename', help='try to look inside compressed files.')
parser.add_argument('-0', '--print0', type=str, nargs='*',
                    metavar='filename', help='terminate filenames with ASCII NUL')
args = parser.parse_args()

args_2 = ['wsl']
args_3 = sys.argv
for file in args_3:
    if len(re.findall('file.py', file)) > 0:
        args_2.append(file.strip('.\\').strip('./').strip('.py'))
    else:
        args_2.append(file)
print(subprocess.run(args_2, shell=True, stdout=subprocess.PIPE).stdout.decode('utf8'))
