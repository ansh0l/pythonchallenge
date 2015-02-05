import urllib, pickle

#hit http://www.pythonchallenge.com/pc/def/pickle.html
#It returns yes! pickle!

url = "http://www.pythonchallenge.com/pc/def/banner.p"

try:
    sock = urllib.urlopen(url)
    pickled_text = sock.read()
    original_object = pickle.loads(pickled_text)
    print original_object
except Exception as e:
    print a, "Done?"

for item in original_object:
    print "".join(i[0] * i[1] for i in item

#prints channel in flowery characters
#url to visit: http://www.pythonchallenge.com/pc/def/channel.html
