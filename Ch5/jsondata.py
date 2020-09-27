import urllib.request
import json

def printResult(data):
	# Use the json module to load the string data into a dictionary
	theJSON = json.loads(data)

	# now we can access the contents of the JSON like any other python object
	if "title" in theJSON["metadata"]:
		print(theJSON["metadata"]["title"])

	# output the number of events, plus the magnitude and each event name
	count = theJSON["metadata"]["count"]
	print (str(count) + " events recorded")


def main():
	urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php"

	# open the URL and read the data 
	webUrl = urllib.request.urlopen(urlData)
	print ("Result code: " + str(webUrl.getcode()))
	if (webUrl.getcode() == 200):
		data = webUrl.read()
		printResult(data)
	else:
		print("Received error, cannot parse results")

if __name__ == "__main__":
	main()