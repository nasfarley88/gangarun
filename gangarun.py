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
parser.add_argument("datafiles", help="specify data/mc file(s)", action="store", nargs='*')
parser.add_argument("-j", "--jobs", help="specify number of jobs (default is 20)", type=int, action="store", default=20)
parser.add_argument("--nosplit", help="when specified, the splitter is not defined.", action='store_true')
parser.add_argument("--browse", help="browse for specified data file", action='store_true')
parser.add_argument("-a","--application", help="specify application being used", default='DaVinci()')
parser.add_argument("--readinputdata",help="specify data .py fie")
parser.add_argument("--dryrun", help="Dry run the program, without submitting or setting up a job", action='store_true')
parser.add_argument("--dirac", help="if specified, job will run on the grid", action='store_true')
parser.parse_args()

args = parser.parse_args()

print args

# Here is where the arguments are taken from the parser
if args.optionsfile:
    optionsFile = args.optionsfile

if not args.datafiles == []:
    dataFiles = args.datafiles
else:
    datafiles = [ 'null string' ]

def submitJob(dataFiles,optionsFile):
    """Function to submit jobs to the grid from a string of data files and a
specifed options file."""
    for i in dataFiles:
        j=Job()

        exec( 'j.application = ' + args.application )
        #j.application = Brunel()
        
        j.application.optsfile=File(optionsFile)

        if args.dirac:
            j.backend=Dirac()
        else:
            j.backend=Interactive()

        if args.nosplit != True:
            j.splitter=SplitByFiles(filesPerJob=args.jobs)

        if args.browse == True:
            data=browseBK()
	elif args.readinputdata == True:
	    # data= + args.application + ".readInputData(" + args.readinputdata + ")")
	    data = j.application.readInputData(args.readinputdata)
        else:
            bkq = BKQuery()
    
            bkq.path = i

            data = bkq.getDataset()

        j.inputdata=data

        j.submit()

if not args.dryrun:
    submitJob(dataFiles,optionsFile)
