import json
import sys
import urllib.request
import urllib.parse
import xmltodict
import logging

'''
    This script will extract a large JSON File and split them into individual chunks.
    Each chunk is then written into a separate file that is named after with EIN 
'''
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("my-logger")

with open("/tmp/index_2019.json",'r') as infile:
    data = json.load(infile)    # read the entire file
    #log.info ( data["Filings2019"]
    for entry in data["Filings2019"]:    # process each EIN Entry
        ein = entry["EIN"]
        logger.info("ein = " + ein)
        url = entry["URL"]
        with open("/tmp/990/" + ein + ".json", 'w') as outfile:    # write file
            #print (json.dumps(entry))
            contents =  urllib.request.urlopen(url)
            #print (json.dumps(xmltodict.parse(contents.read())))
            detailsStr = json.dumps(xmltodict.parse(contents.read()))
            # print (detailsStr)
            # user json.loads to load string
            detailsJson = json.loads(detailsStr)
            # print (detailsJson["Return"])
            # Inject the Return object into the entry
            entry["Return"] = detailsJson["Return"]
            json.dump(entry, outfile, indent=4)
