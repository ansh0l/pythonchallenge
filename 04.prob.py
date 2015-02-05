import urllib
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
nothing = lambda x='': "?nothing=%s" % x

query = ''
try:
    while True:
        sock = urllib.urlopen(url + nothing(query))
        text = sock.read()
        query = text.split()[-1]
        print query, text
except:
    print "Done?"
