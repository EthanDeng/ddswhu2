# DownloadHelper Ver 1.0
# Copyright by EthanDeng 2015
# Author: ddswhu (http://ddswhu.com/)
# Email: ddswhu@outlook.com
# Last Modified: 2015/3/25

# coding = UTF-8
import urllib2
import re

# open the url and read
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re,html)
    obfile.write('\n'.join(url_lst))
    obfile.write('\n')
    obfile.close()
    return(url_lst)

def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r" %10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()

# write the url into a txt file
obfile = open('url.txt','a+')

# example : http://www.princeton.edu/~otorres/
print "Welcome to Download Helper Guide!\n     Designed by EthanDeng"
raw_url = raw_input("Please input the website url (raw_url): \n")
complete_judge = raw_input("The url is complet or not? (Y/N) ")
if complete_judge == 'N':
    raw_judge = raw_input("The root url is the website url? (Y/N) ")
    if raw_judge == "Y":
        root_url = raw_url
    else:
        root_url = raw_input("What's the root url ?\n")
else:
    root_url = ''

html = getHtml(raw_url)
url_lst = getUrl(html)


for url in url_lst[:]:
    url = root_url + url
    getFile(url)
