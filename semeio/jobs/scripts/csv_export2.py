import argparse
import os
import sys

import pandas as pd
from fmu import ensemble
from res.enkf import ErtScript
from semeio.jobs.csv_export2 import csv_export2


class CsvExport2Job(ErtScript):
    def run(self, *args):
        main(args)


def main(args):
    """Setup parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument("runpathfile", type=str)
    parser.add_argument("outputfile", type=str)
    parser.add_argument("time_index", type=str, default="monthly")
    parser.add_argument("column_keys", nargs="+", default=None)
    args = parser.parse_args(args)

    csv_export2.csv_exporter(
        runpathfile=args.runpathfile,
        time_index=args.time_index,
        outputfile=args.outputfile,
        column_keys=args.column_keys,
    )

    print("{} csv-export written to {}".format(args.time_index, args.outputfile))


if __name__ == "__main__":
    main(sys.argv[1:])
