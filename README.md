gangarun
========

A small script designed to run simple ganga jobs based on a pre-prepared options file.

It was made to make submitting jobs to the grid simpler, especially when almost all ganga files (for me at least) are the same.

Roadmap
-------
Current items are todo
- Figure out how to pass a list for data files
- Configure the syntax to be:
  - gangarun.py OPTIONSFILE DATAFILE1 [DATAFILE2 ...] [OPTIONS]
- Configure argparse for number of jobs
- Configure argparse for DaVinci version


Even further down the road
--------------------------
- Automatic sensing which py file is data and which is an options (meaning the user could put OPTIONSFILE and DATAFILE in any order)
- Logo.
