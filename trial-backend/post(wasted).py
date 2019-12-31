from google import google
import urllib.request
import re
num_page = 1
s = google.search("AIDS", num_page)
print(len(s))
'''
for i in s:
   print('Link:',i.link,'\n','Decrp:',i.description)
''' 
print('parsing site..')  
i=0
while(True):
   if(s[i].link!=None):
      url=s[i].link
      print(url)
      req = urllib.request.Request(url)
      resp = urllib.request.urlopen(req)
      respData = resp.read()
      paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
      for eachP in paragraphs:
         print(eachP)
      break
   i+=1
