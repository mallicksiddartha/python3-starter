import urllib.request as urlReq
import urllib.parse as urlPar

#x = urlReq.urlopen('https://www.google.com')
#print(x.read())
'''
url = 'http://pythonprogramming.net'
values = {'s' : 'basic',
          'submit' : 'search'}
data = urlPar.urlencode(values)
data = data.encode('ascii')
req = urlReq.Request(url)
resp = urlReq.urlopen(req)
respData = resp.read()

print(respData)
'''

try:
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    reqq = urlReq.Request('https://www.google.com/search?q=test', headers=headers)
    print(reqq.get_header("User-Agent", "hhhhhh"))
    googleSearch = urlReq.urlopen(reqq)
    #print(googleSearch.read())

    savedFile = open('searchedText.txt', 'w')
    savedFile.write(str(googleSearch.read()))
    savedFile.close()
except Exception as ex:
    print(str(ex))
