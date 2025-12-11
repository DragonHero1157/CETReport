"""
Docstring for Modules.CommandLine
    Contains the functions that support processing and accessing the application command line and its arguments.

Contents:
    Classes:
        Args is an object that configures the help text and command line argument specifications
"""
import argparse
from dataclasses import dataclass, field

class Args():
    inFName = field(default_factory=str)
    outFname = field(default_factory=str)

    def __init__(self):
        argvparser = argparse.ArgumentParser(description="A script that parses a CSV file into unique records.")
        # Define the mandatory and optional command line arguments
        argvparser.add_argument("-in", "--inFName", required=True, help="Name of the input CSV file (can be fully or relatively pathed)")
        argvparser.add_argument("-out", "--outFName", required=True, help="Name of the output CSV file (can be fully or relatively pathed)")
        argvparser.add_argument("-d", "--dump", action="store_true", help="(optional) Enable dump of raw data records")

        # Get the actual command line arguments
        myArgv = argvparser.parse_args()

        # Store arguments
        self.inFName: str = myArgv.inFName
        self.outFName: str = myArgv.outFName
        self.doDump: bool = myArgv.dump