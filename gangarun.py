#!/usr/bin/env ganga

import sys
import argparse


# Taken from
# http://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

# Pay attention:
# the f in file is capitalised for the 'local' copies of these variables so
# optionsfile -> optionsFile etc.
parser = argparse.ArgumentParser(description='Small script to run ganga job')
parser.add_argument("optionsfile", help="specify options file", action="store")
parser.add_argument("datafiles", help="specify data/mc file(s)", action="store", nargs='+')
parser.parse_args()

args = parser.parse_args()

print args

# Here is where the arguments are taken from the parser
if args.optionsfile:
    optionsFile = args.optionsfile
# else:
#     print "No options file specified"
#     sys.exit()

if args.datafiles:
    dataFiles = args.datafiles
# else:
#     print "No data/mc file specified"
#     sys.exit()

def submitJob(dataFiles,optionsFile):
    """Function to submit jobs to the grid from a string of data files and a
specifed options file."""
    for i in dataFiles:
        j=Job()
        j.application=DaVinci(version="v34r0")

        j.application.optsfile=File(optionsFile)

        j.backend=Dirac()
        # j.backend=Interactive()

        j.splitter=SplitByFiles(filesPerJob=20)

        bkq = BKQuery()

        bkq.path = i

        data = bkq.getDataset()

        j.inputdata=data

        j.submit()

submitJob(dataFiles,optionsFile)
