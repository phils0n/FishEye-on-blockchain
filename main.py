from sqlConnect import *
from inputData import *
from retriveData import *
import json
import ast 
import simplejson

#f = open('example_2.json')
#data = json.load(f)
#data = str(data)

#data = data.encode('utf-8').hex()
#dataSent = []

#postData(data, dataSent)

transactionID = input("Id you want information about")
s = getData(getFromSql(transactionID)[1])





sourceFile = open('demo3.json', 'w')
s = ast.literal_eval(s)
print('\n' + (json.dumps(s, indent=4)), file = sourceFile)
sourceFile.close()
