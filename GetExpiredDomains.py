#
# GetExpiredDomains
# Search for available domain from expireddomains.net
# By: 3gstudent
# License: BSD 3-Clause

import urllib
import urllib2
import sys

from bs4 import BeautifulSoup

def GetResults(loop,key):
    for i in range(1,loop):
        print "[+]Page %d" %(i+1)
        url = "https://www.expireddomains.net/domain-name-search/?start=" + str(25*i) + "&q="+ key
        #print url
        req = urllib2.Request(url)
        #req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")   
        res_data = urllib2.urlopen(req)
        html = BeautifulSoup(res_data.read(), "html.parser")
 
        tds = html.findAll("td", {"class": "field_domain"})
        for td in tds:
            print td.findAll("a")[0]["title"]
   
def SearchExpireddomains(key):
    url = "https://www.expireddomains.net/domain-name-search/?q=" + key 
    req = urllib2.Request(url)
    #req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")  
    res_data = urllib2.urlopen(req)
    html = BeautifulSoup(res_data.read(), "html.parser")
    Result = html.select('strong')[0].text.replace(',', '')
    print "[*]Total results: %s" % Result

    if int(Result) <25:
        return
    elif int(Result) > 550:
        print "[!]Too many results,only get 550 result."
        print "[*]21 requests will be sent."

        print "[+]Page 1"
        tds = html.findAll("td", {"class": "field_domain"})
        for td in tds:
            print td.findAll("a")[0]["title"]
        GetResults(21,key)

    else:
        print "[*]%d requests will be sent." % (int(Result)/25+1)

        print "[+]Page 1"
        tds = html.findAll("td", {"class": "field_domain"})
        for td in tds:
            print td.findAll("a")[0]["title"]
        GetResults(int(Result)/25+1,key)

if __name__ == "__main__":
    print "GetExpiredDomains - Search for available domain from expireddomains.net"
    print "Author: 3gstudent\n"

    if len(sys.argv)!=2:
        print ('Usage:')
        print ('    GetExpiredDomains.py <Search String>')   
        sys.exit(0)    
    SearchExpireddomains(sys.argv[1])
    print "[*]All Done"
