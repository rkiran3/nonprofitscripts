import json
import csv
import sys
import urllib.request
import urllib.parse
import xmltodict

'''
    This script will write an sql INSERT statement with values extracted
    from the input file.
'''
eins = []
csvrow = []

csvfile = open("/tmp/irs_eins.csv", 'w', newline='')
writer = csv.writer(csvfile, dialect='excel')

''' output file '''
sqlfile = open("/tmp/irs_eins_insert.txt", 'w', newline='')

print ('Start')
with open("/tmp/index_2019.json",'rb') as infile:
    data = json.load(infile)    # read the entire file
    for entry in data["Filings2019"]:    # process each EIN Entry
        ein = entry["EIN"]
        taxPeriod = entry["TaxPeriod"].strip()
        formType = entry["FormType"].strip()
        orgName = entry["OrganizationName"]
        url = entry["URL"]
        csvrow = [ein, taxPeriod, formType, orgName, url]
        
        #print ('writing ' , csvrow)
        writer.writerow(csvrow)

        sqlins = 'insert into polls_taxform (ein, taxperiod, formtype, orgname, url) values ("{0}", "{1}", "{2}", "{3}", "{4}");\n'.format(ein, taxPeriod, formType, orgName, url)
        sqlfile.write(sqlins)
        sqlfile.write('')

csvfile.close()        
        
print ('End')
                
