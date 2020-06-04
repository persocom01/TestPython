# Demonstrates reading and writing files in csv format.
import re
import csv
import os

file = './files/DAILYDATA_S116_201912.csv'


# Cleans column names for easier processing later.
def csv_clean_colnames(file, sep=''):
    '''
    Given the path to a csv file, this function cleans the column names by
    converting removing leading and trailing white spaces, converting all
    letters to lowercase, replacing all remaining whitespaces with
    underscores, removing brackets and other special characters. The csv
    file is then replaced with a copy of itself with the cleaned column
    names.

    params:
        file        path of file wholse column names are to be cleaned.
        sep         The character(s) used to replace brackets and special
                    characters.
    '''

    def remove_special_characters(text, sep=sep):
        pattern = r'[^a-zA-Z0-9!"#$%&\'()*+, -./:; <= >?@[\]^_`{|}~]'
        return re.sub(pattern, sep, text)

    # Opens the csv file and writes the cleaned version to a .tmp file.
    tempfile = file + '.tmp'
    with open(file, 'r') as infile, open(tempfile, 'w', newline='') as outfile:
        r = csv.reader(infile, delimiter=',', quotechar='"')
        colnames = next(r)
        colnames = [remove_special_characters(x.strip().lower().replace(' ', '_').replace('(', sep).replace(')', sep).replace('/', sep)) for x in colnames]

        w = csv.writer(outfile)
        w.writerow(colnames)
        for i, row in enumerate(r):
            if i > 0:
                w.writerow(row)

    # Delete original and replace it with the cleaned file.
    os.remove(file)
    os.rename(tempfile, file)


csv_clean_colnames(file, sep='')
