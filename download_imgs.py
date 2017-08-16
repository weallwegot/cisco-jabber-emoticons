import json
import base64
import os

with open('pics_data.json','r') as infile:
	imgs = json.load(infile)
infile.close()

for key, value in imgs.iteritems():
	try:
		img_data = value.split("base64,")[1]
		key_transformed = key.replace('(','').replace(')','').replace('&','').replace("\'",'').encode("utf8").lower()

		img_file_path = 'imgs'+ os.sep + key_transformed + '.png' 
		print img_file_path
		with open(img_file_path, "wb") as fh:
		    fh.write(base64.b64decode(img_data))
		fh.close()
	except Exception as e:
		print 'There was an error'
		print e
