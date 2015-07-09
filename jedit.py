import json
f=open ("test.json","r+")
data=json.load(f)
print data
data['id']=144
f.seek(0)
#json.dump(data,f,indent=4)
json.dumps("{\"navneet\",\"name\"}",f,indent=4)
print type(data)
f.close()
