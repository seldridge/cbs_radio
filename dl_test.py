import urllib,os.path,re
top_file = 'top.html'
download_dir = './downloads'
current_file = 'current.html'
top_url = 'http://www.cbsrmt.com/'
list_url = '?s=synopsis&y=all'
number_to_find = 1399
sub_url = 'http://www.cbsrmt.com/episode-1-the-old-ones-are-hard-to-kill.html'

urllib.urlretrieve(sub_url,current_file)
if not(os.path.exists(download_dir)):
    print 'creating directing',download_dir
    os.mkdir(download_dir)
else:
    print 'directory',download_dir,'already exists'
sub = open(current_file,'r')
for sub_line in sub:
    if re.search('\.mp3',sub_line):
        dl_link = re.findall('mp3/.*?\.mp3',sub_line)
        dl_link[0] = re.sub(' ','%20',dl_link[0])
        episode_num = re.findall('e[0-9]{4}',dl_link[0])
        episode_num[0] = re.sub('e','',episode_num[0])
        print top_url+dl_link[0],'->',download_dir+'/'+episode_num[0]+'.mp3'
#        urllib.urlretrieve(top_url+dl_link[0],download_dir+episode_num[0]+'.mp3')
sub.close()
