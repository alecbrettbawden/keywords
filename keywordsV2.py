import gzip
import xml.etree.ElementTree as ET

# Read gzip XML and created nested list of Keyword Groups
f = gzip.open('keywords.xml.gz', 'rb')
kl = [str(kw.text).split(' -')[0].split() for kw in ET.parse(f).getroot().iter('Keyword')]
f.close()

# Global Constants
r1 = {}
r2 = {}
r3 = {}
er = ''

# Get 1st, 2nd, 3rd Keyword Relations
[r1.update({(q := i.copy()).pop(c):q}) if k not in r1 else r1.update({(q := i.copy()).pop(c):q+r1[k]}) for i in kl for c, k in enumerate(i)]
[r2.update({i:(q := list(filter(lambda a: a not in r1[i] and a != i,r1[x])))}) if i not in r2 else r2.update({i:r2[i]+(q := list(filter(lambda a: a not in r1[i] and a != i,r1[x])))}) for i in r1 for x in set(r1[i])]
[r3.update({i:(q := list(filter(lambda a: a not in r1[i] and a not in r2[i] and a != i,r1[x])))}) if i not in r3 else r3.update({i:r3[i]+(q := list(filter(lambda a: a not in r1[i] and a not in r2[i] and a != i,r1[x])))}) for i in r1 for x in set(r2[i])]

# Count occurrences and sort by count
for r in [r1,r2,r3]:
    for i in r:
        r[i] = dict(zip(r[i],list(map(lambda x: r[i].count(x), r[i]))))
        r[i] = {k: v for k, v in sorted(r[i].items(), key=lambda item: item[1], reverse=True)}

# # Turn the results dictionary into an XML readable string
for i in r1:
    xml = """\n\t<Item>\n\t\t<Keyword>{0}</Keyword>""".format(i)
    for c, r in enumerate([r1,r2,r3]):
        xml += '\n\t\t<{0}degree>{1}</{0}degree>'.format(c+1,r[i])
    xml += '\n\t</Item>'
    er += xml
er = '<ItemList>{0}\n</ItemList>'.format(er)

# # Save r1 string into a new xml file within the directory
f = open("Results.xml", "wb")
f.write(er.encode())
f.close()