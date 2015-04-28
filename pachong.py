import urllib
urls = {'http://www.chinaai.org/Article_Show.asp?ArticleID=315':'prolog2.html'}
new_tag = ""

for url in urls:
filename = urls[url]
urllib.urlretrieve(url,filename)
f = open(filename,'r')
content = f.read()
f.close()

l_pos = content.find('<body')
r_pos = content.find('>', l_pos)
cont1 = content[:l_pos]
cont2 = content[r_pos + 1:]
content = cont1 + new_tag + cont2
f = open('tmp.html','w')
f.write(content)
f.close()