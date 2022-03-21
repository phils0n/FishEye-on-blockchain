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
print(getFromSql("0x2556cc9317a0e5167a554910a3eda244e088bd8af337bba3ce8f1b23e7a3d76c"))




#sourceFile = open('demo2.json', 'w')
#s = ast.literal_eval(s)
#print('\n' + (json.dumps(s, indent=4)), file = sourceFile)
#sourceFile.close()
