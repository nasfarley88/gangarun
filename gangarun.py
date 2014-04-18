#!/usr/bin/env ganga

import sys
import argparse

parser = argparse.ArgumentParser(description='Small script to run ganga job')
parser.add_argument("-o", "--optionsfile", help="specify options file", action="store")
parser.add_argument("-d", "--datafile", help="specify data/mc file", action="store")
parser.parse_args()

args = parser.parse_args()

if args.optionsfile:
    optionsFile = args.optionsfile
else:
    print "No options file specified"
    sys.exit()

if args.datafile:
    dataFiles = [ args.datafile ]
else:
    print "No data/mc file specified"
    sys.exit()

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

        #bkq.path = "/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-BcVegPy/Sim08d/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/14103020/ALLSTREAMS.DST"
        bkq.path = i

        data = bkq.getDataset()

        j.inputdata=data

        j.submit()

submitJob(dataFiles,optionsFile)
