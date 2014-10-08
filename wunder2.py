import urllib2
import json

wurl = urllib2.urlopen("http://api.wunderground.com/api/92827660840d7850/history_20140601/q/DC/Washington.json")

json_string = wurl.read()
parsed_json = json.loads(json_string)

print parsed_json

wurl.close()
