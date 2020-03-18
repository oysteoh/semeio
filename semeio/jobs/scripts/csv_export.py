#!/usr/bin/env python

import sys
from ert_shared.storage import storage_api
import pandas as pd


def main(args):
    #parser = create_parser()
    #parsed_args = parser.parse_args(args)

   # responses = pd.DataFrame(columns="Realization")
    for response in storage_api.get_response_data("POLY_RES", "default"):
        print(response)

if __name__ == "__main__":
    main(sys.argv[1:])