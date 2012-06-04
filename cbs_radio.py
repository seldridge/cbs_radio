import urllib,os.path,re
top_file = 'top.html'
top_url = 'http://www.cbsrmt.com/?s=synopsis&y=all'
number_to_find = 1399
if not(os.path.exists(top_file)):
    print 'file',top_file,'not found...\n','Fetching it from',top_url
    urllib.urlretrieve(top_url,top_file)
else:
    print 'file',top_file,'already exists... not fetching'
top = open(top_file,'r')
pages = []
count = 0
for line in top:
    if re.match('.+?<td><a href=\'./episode-.+?</td>.*',line):
        page = re.findall('\'.+?\'',line) # only need one value, though...
        page[0] = re.sub('\'[\.]*','',page[0]);
        pages.append(page[0])
        count += 1
print 'found',count,'subpages'
top.close()
