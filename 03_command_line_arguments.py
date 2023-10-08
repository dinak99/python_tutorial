"""
Usage:
python3 03_command_line_arguments.py foo bar -h 123

Try also:
import getopt
import argparse
"""
import sys

print(type(sys.argv))
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

print('The command line arguments are:')
for i in sys.argv:
    print(i)
