#!/usr/bin/env python3
# File name: keywords.py
# Description: abowcut/keywords 

import gzip
import xml.etree.ElementTree as ET


# Read gzip XML and created nested list of Keyword Groups
def parse_xml(xml):    
    f = gzip.open(xml, 'rb')
    kl = [str(kw.text).split(' -')[0].split() for kw in ET.parse(f).getroot().iter('Keyword')]
    f.close()

    return kl

# Create first level mappings
def map_first_relations(parsed_words):
    r = {}
    for k in parsed_words:
        for i in k:
            if i not in r : r[i] = {}
            for x in list(filter(lambda a: a != i, k)):
                r[i][x] = 1 if x not in r[i] else r[i][x]+1
            r[i] = {m: v for m, v in sorted(r[i].items(), key=lambda item: item[1], reverse=True)}
    
    return r

# Create Nth level mappings
def map_n_relations(data, n):
    for q in range(n-1):
        for k in data:
            if isinstance(data[k], list) == False: data[k] = [data[k]] + [{} for i in range(n-1)]
            for m in data[k][q]:
                if isinstance(data[m], list) == False: data[m] = [data[m]] + [{} for i in range(n-1)]
                p = {k:1}
                [p.update(data[k][n]) for n in range(q+1)]
                for i in list(filter(lambda a: a not in p, data[m][0])):
                    data[k][q+1][i] = 1 if i not in data[k][q+1] else data[k][q+1][i]+1
            data[k][q+1] = {m: v for m, v in sorted(data[k][q+1].items(), key=lambda item: item[1], reverse=True)}
    
    return data

# Turn the results dictionary into an XML readable string and save to local directory
def results_to_xml(data):
    er = ''
    for i in data:
        xml = '\n\t<Item>\n\t\t<Keyword>{0}</Keyword>'.format(i)
        for m, t in enumerate(data[i]):
            xml += '\n\t\t<{0}degree>{1}</{0}degree>'.format(m+1,t)
        xml += '\n\t</Item>'
        er += xml
    er = '<ItemList>{0}\n</ItemList>'.format(er)
    f = open("Results.xml", "wb")
    f.write(er.encode())
    f.close()
    print('Saved Results.xml to local directory')

# Main Function (Begin Here)
def main():
    keyword_list = parse_xml('keywords.xml.gz')
    res = map_first_relations(keyword_list)
    end = map_n_relations(res, 3)
    results_to_xml(end)


if __name__ == '__main__':
    main()