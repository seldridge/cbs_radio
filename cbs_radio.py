import urllib,os.path,re
top_file = "top.html"
top_url = "http://www.cbsrmt.com/?s=synopsis&y=all"
if not(os.path.exists(top_file)):
    print "File "+top_file+" not found...\n","Fetching it from "+top_url
    urllib.urlretrieve(top_url,top_file)
else:
    print "File "+top_file+" already exists... not fetching"
top = open(top_file,"r")
for line in top:
    if re.match(".+?<td><a href='./episode-.+?</td>.*",line):
        print line
top.close()
