import urllib2 as URL

k = URL.urlopen('http://orlindustries.com/olp/device_pull?device_api_key=155210e2c404c70da7bdf2ced4ed0b81').read()
print k



