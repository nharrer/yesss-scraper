import os
from bs4 import BeautifulSoup

def parse(outputdir, pagefile):
    columnheader = []
    rows = []
    page = 1
    found = True
    while found:
        page = page + 1
        filename = pagefile.replace('{page}', str(page))
        inputfile = os.path.join(outputdir, filename)
        found = os.path.exists(inputfile)
        if found:
            with open(inputfile, mode='r', encoding='utf-8') as file:
                print(f"Parsing file {inputfile}.")
                content = file.read()
                soup = BeautifulSoup(content, features='html.parser')
                for list in soup.find_all(class_='list-group'):
                    rows.append(parse_list_group(list, columnheader))
    return [columnheader, rows]

def parse_list_group(soup, columnheader):
    columns = {}
    for item in soup.select('.list-group-item'):
        headerline = ''
        textline = ''
        for col in item.select(".row [class^='col-']"):
            if col.has_attr('class'):
                if 'bold' in col['class']:
                    headerline = col.text
                else:
                    textline = col.text
        if headerline != '':
            headerline = headerline.replace(':', '')
            if headerline == 'Datum/Uhrzeit':
                textline = textline.replace(' ', '/')
            headerparts = headerline.split('/')
            textparts = textline.split('/')
            if len(headerparts) == len(textparts):
                for idx, header in enumerate(headerparts):
                    text = textparts[idx]
                    handle_column(header, text, columnheader, columns)
            else:
                handle_column(headerline, textline, columnheader, columns)
    return columns

def handle_column(header, text, columnheader, columns):
    if (header == 'Upload' or header == 'Download'):
        value = float(text[0:-3].replace(',', '.'))
        if text.endswith('KB'):
            value = value / 1024
        elif text.endswith('MB'):
            pass
        else:
            raise Exception(f"Invalid unit {text[-2:]}' in {text}")
        text = str(value).replace('.', ',')

    if (header == 'Kosten'):
        text = text.replace('\u20ac', '')

    if not header in columnheader:
        columnheader.append(header)

    columns[header] = text
