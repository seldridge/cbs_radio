import urllib,os.path,re,sys,linecache
download_dir = './downloads'
top_file = 'top.html'
current_file = 'current.html'
dl_list = 'dl_list.txt'
top_url = 'http://www.cbsrmt.com/'
list_url = '?s=synopsis&y=all'
number_dls = 10

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
if not(os.path.isfile(dl_list)):
    dl = open(dl_list,'w')
    for line in top:
        if re.match('.+?<td><a href=\'./episode-.+?</td>.*',line):
            page = re.findall('\'.+?\'',line) # only need one value, though...
            page[0] = re.sub('\'\.?\/?','',page[0])
            pages.append(page[0])
            count += 1
#            print '  exploring page',top_url+page[0]
            urllib.urlretrieve(top_url+page[0],current_file)
            sub = open(current_file,'r')
            for sub_line in sub:
                if re.search('\.mp3',sub_line):
                    dl_link = re.findall('mp3/.*?\.mp3',sub_line)
                    dl_link[0] = re.sub(' ','%20',dl_link[0])
#                    print top_url+dl_link[0],'->',download_dir+'/'+episode_num[0]+'.mp3'
                    dl.write(top_url+dl_link[0]+'\n')
            if (count%(1399/100)==0):
                print ' ',count/(1399/100),'percent done!'
            sub.close()
            sys.stdout.flush()
    print 'found',count,'subpages'
    dl.close()

for i in range(number_dls):
    line = linecache.getline(dl_list,i+1)
    episode_num = re.findall('e[0-9]{4}',line)
    episode_num[0] = re.sub('e','',episode_num[0])
    episode_name = re.findall('e[0-9]{4}.*\.mp3',line)
    episode_name[0] = re.sub('e[0-9]{4}','',episode_name[0])
    episode_name[0] = re.sub('\%20','.',episode_name[0])
    if not(os.path.exists(download_dir+'/'+episode_num[0]+episode_name[0])):
        print '  downloading',download_dir+'/'+episode_num[0]+episode_name[0]
        urllib.urlretrieve(line,download_dir+'/'+episode_num[0]+episode_name[0])
        sys.stdout.flush()
    else:
        print '  Warning! File',download_dir+'/'+episode_num[0]+episode_name[0],'already exists!'
        sys.stdout.flush()
#    print episode_name[0]
#    print top_url+line,'->',download_dir+'/'+episode_num[0]+episode_name[0]
#    print download_dir+'/'+episode_num[0]+episode_name[0]
    linecache.clearcache()

top.close()
