#!/usr/local/bin/ python

import re
import csv
import argparse


def arguments():
    """
    Parse command line arguments

    @return filename (string)
    """

    parser = argparse.ArgumentParser(description="txt file location.")
    parser.add_argument("-f", "--file", default="", help="Path of the txt file.", required=True)

    args = parser.parse_args()
    return args.file


def main(filename):
    """
    The main function
    """
    filename_csv = filename.replace('.txt', '.csv')

    # Create csv file
    csv_data = open(filename_csv, 'w')

    # Open txt file
    with open(filename, 'r') as f:
        for line in f:
            line = re.sub(',', '', line)
            new_line = re.sub('\s\s+', ',', line)
            csv_data.write(new_line)
    f.close()


if __name__ == "__main__":

    filename = arguments()
    main(filename)