import urllib,os.path,re,sys
download_dir = './downloads'
top_file = 'top.html'
current_file = 'current.html'
top_url = 'http://www.cbsrmt.com/'
list_url = '?s=synopsis&y=all'
number_to_find = 1399

if not(os.path.exists(top_file)):
    print 'file',top_file,'not found...\n','Fetching it from',top_url+list_url
    urllib.urlretrieve(top_url+list_url,top_file)
else:
    print 'file',top_file,'already exists... not fetching'

if not(os.path.exists(download_dir)):
    print 'creating directing',download_dir
    os.mkdir(download_dir)
else:
    print 'directory',download_dir,'already exists'

top = open(top_file,'r')
pages = []
count = 0
print 'starting search...'
for line in top:
    if re.match('.+?<td><a href=\'./episode-.+?</td>.*',line):
        page = re.findall('\'.+?\'',line) # only need one value, though...
        page[0] = re.sub('\'\.?\/?','',page[0])
        pages.append(page[0])
        count += 1
        print '  exploring page',top_url+page[0]
        urllib.urlretrieve(top_url+page[0],current_file)
        sub = open(current_file,'r')
        for sub_line in sub:
            if re.search('\.mp3',sub_line):
                dl_link = re.findall('mp3/.*?\.mp3',sub_line)
                dl_link[0] = re.sub(' ','%20',dl_link[0])
                episode_num = re.findall('e[0-9]{4}',dl_link[0])
                episode_num[0] = re.sub('e','',episode_num[0])
                print top_url+dl_link[0],'->',download_dir+'/'+episode_num[0]+'.mp3'
        sub.close()
        sys.stdout.flush()
print 'found',count,'subpages'
top.close()
