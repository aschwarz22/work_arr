import urllib.request



def get_url(digikeyID):
    with urllib.request.urlopen('https://www.digikey.com/products/en?keywords=' + digikeyID) as url:
        s = url.read()
    s = str(s)
    s = s.split('\\n')
    for line in s:
        if "lnkDatasheet" in line:
            line = line.strip(' ').split(' ')
            urlLine = line[3]
            url = urlLine.strip('href=').strip('"')
            return url


def url_assoc(fkey, mfg, fout):
    f = open(fkey, "r")
    m = open(mfg, "r")
    w = open(fout, "w")
    count = -1
    for line in f:
        count += 1
        url = get_url(line)
        if line == None or url == None:
            print (count)
            for i, item in enumerate(m):
                if i == count:
                    url = get_url(item)
                    break
            if url == None:
                w.write('\n')
            else:
                w.write(item[:-1] + '-->-->--' + url + '\n')
            continue
        w.write(line[:-1] + '-->-->--' + url + '\n')
        if '277-2205-ND' in line:
            break
    f.close()
    w.close()


fin = 'digiIDs.txt'
fmfg = 'mfgpn.txt'
fout = 'IDs.txt'
url_assoc(fin, fmfg, fout)