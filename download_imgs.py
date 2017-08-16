import json
import base64

with open('pics_data.json','r') as infile:
	imgs = json.load(infile)
infile.close()

for key, value in imgs.iteritems():
	try:
		img_data = value.split("base64,")[1]
		with open(key + ".png", "wb") as fh:
		    fh.write(base64.b64decode(img_data))
		fh.close()
	except Exception as e:
		print 'There was an error'
		print e
