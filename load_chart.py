import os
import urllib2
import textgraph

height, width = os.popen('stty size', 'r').read().split()
height = int(height)
width  = int(width)

hosts = [
    "rein.utsc.utoronto.ca",
    "rein001.utsc.utoronto.ca",
    "rein002.utsc.utoronto.ca",
    "rein003.utsc.utoronto.ca",
    "rein004.utsc.utoronto.ca",
    "rein005.utsc.utoronto.ca",
    ]

data = []
for host in hosts:
    url = "http://localhost/ganglia/graph.php?r=hour&h=%s&m=load_one&s=by+name&mc=2&g=load_report&c=utsc&csv=1"%host

    request = urllib2.Request(url)
    csv = urllib2.urlopen(request).readlines()

    one = []
    one.append(1.)

    for l in csv[-(width-1):]:
        c = l.split(",")
        if c[1] == "NaN":
            v = 0.
        else:
            try:
                v = float(c[1])
            except: 
                v =0.
        one.append(v)
    data.append(one)

for i,host in enumerate(hosts):
    print textgraph.vertical_graph(data[i], height=(height)/len(hosts)-1)
