# webscraping library parser
print "HI!!!!!!!!!!!!!!!!!!!!!!!!!!"
import lxml.html
import requests
from collections import OrderedDict
import json

# webscraping library w/ easier syntax
from bs4 import BeautifulSoup, SoupStrainer

print "#$UJ#(*H$OI#NO$NONIO#N$O@N#O$)"


headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30"}
try:
	response = requests.get("http://unicode.org/emoji/charts/full-emoji-list.html",headers=headers)
except requests.exceptions.RequestException as e:
	print 'There was an error'
	print e
except requests.exceptions.ConnectionError as e:
	print e
emoji_html = response.content
# sub set of the full page that only includes tags with attributes of border=1.
# (this is the giant table with all the emojis)
only_the_large_important_table = SoupStrainer(attrs={"border":"1"})

soup_table = BeautifulSoup(emoji_html,"lxml",parse_only=only_the_large_important_table)

# list will hold tuples (key, value) pair for each emoji
# key: name of the emoji
# value: the link to the image source
# use list to preserve order
super_list = []
# get all of the rows of the table
all_table_rows = soup_table.find_all('tr')
# the index that corresponds to the tag with a specific platform img
index_dict = {'apple_emoji':6}
# size of tags with legitimate content in them
for tr_tag in all_table_rows:
	# because there are some rows that only have a few elements
	# these are the rows that dont have the emoji pictures in them.
	if len(tr_tag) == 32:
		try:
			image_src_string = tr_tag.contents[index_dict['apple_emoji']].img['src']
			for child in tr_tag.contents:
				# some of new line characters get picked up as children. we want to skip those
				if not child == '\n':
					class_name = child['class']
					if class_name[0] == 'name':
						# replace spaces with underscores so they can eventually be used as file names
						emoji_name = child.string.replace(' ','_').replace(':','').replace('.','').replace('!','').replace(',','').replace('-','_')
						#super_dictionary[emoji_name] = image_src_string
						good_tuple = (emoji_name,image_src_string)
						super_list.append(good_tuple)
		except:
			continue
with open('pics_data.json','w') as outfile:
	json.dump(OrderedDict(super_list),outfile)
