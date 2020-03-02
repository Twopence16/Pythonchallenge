'''
#level 2
import requests
import re
url = r'http://www.pythonchallenge.com/pc/def/ocr.html'
webtext=requests.get(url).text
pattern=re.compile(r'<!--(.*?)-->',re.S)
hiddentext = re.findall(pattern,webtext)
print(hiddentext[0])
level2answer=''.join([text for text in re.findall(r'[a-z]+',hiddentext[1])])
print(level2answer)
'''

'''
#level 3
import requests
import re
url=r'http://www.pythonchallenge.com/pc/def/equality.html'
webtext=requests.get(url).text
pattern=re.compile(r'<!--(.*?)-->',re.S)
hiddentext=re.findall(pattern,webtext)
#print(len(hiddentext))
#print(hiddentext[0])
pattern=re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]',re.S)
level3answer=''.join([text for text in re.findall(pattern,webtext)])
print(level3answer)
'''

'''
#level 4 http://www.pythonchallenge.com/pc/def/linkedlist.php
import requests
import re
payload={'nothing':'12345'}
url=r'http://www.pythonchallenge.com/pc/def/linkedlist.php'
attemptnumber=0
webtext=''
while attemptnumber<=400:
    webtext=requests.get(url,params=payload).text
    print(webtext)
    nothingnumber=re.findall(r'[0-9]+',webtext)
    if nothingnumber:
        payload['nothing']=nothingnumber[len(nothingnumber)-1]
    elif 'Divide' in webtext:
        payload['nothing']= str(int(payload['nothing'])/2)
    else:
        break
    attemptnumber=attemptnumber+1
'''

#level5 http://www.pythonchallenge.com/pc/def/peak.html


    



