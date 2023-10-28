import os
from secret import secrets
from pathlib import Path

from scraper import scrape
from webparser import parse

BASEURL = 'https://www.yesss.at/kontomanager.at/'
OUTPUTDIR = 'output'
PAGEFILE = 'page{page}.html'
CSVFILE = 'output.csv'
SCRAPE = True

if __name__ == '__main__':
    if SCRAPE:
        scrape(BASEURL, secrets['USERNAME'], secrets['PASSWORD'], OUTPUTDIR, PAGEFILE)

    [columnheader, rows] = parse(OUTPUTDIR, PAGEFILE)

    csvfile = os.path.join(OUTPUTDIR, CSVFILE)
    print(f"Writing csv to file {csvfile}.")
    with open(csvfile, 'w', encoding='iso-8859-1') as file:
        for header in columnheader:
            file.write(f'{header};')
        file.write('\n')
        for row in rows:
            for header in columnheader:
                text = row[header]
                file.write(f'{text};')
            file.write('\n')
