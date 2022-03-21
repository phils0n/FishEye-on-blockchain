from sqlConnect import *
from inputData import *
from retriveData import *
import json
import ast 
import simplejson

#f = open('example_2.json')
#data = json.load(f)
#data = str(data)
#print(data)


#text ="Hello world"
#data = data.encode('utf-8').hex()
#dataSent = []

#postData(data, dataSent)
#getData(getFromSql())
s = getData("0x5fc2886e994405ad8f7abda8c1d02cde37e049b423b884e413b6e05a0a3737e3")

sourceFile = open('demo1.json', 'w')
s = ast.literal_eval(s)
print('\n' + (json.dumps(s, indent=4)), file = sourceFile)
sourceFile.close()
