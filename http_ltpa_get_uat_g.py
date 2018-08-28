import requests
from bs4 import BeautifulSoup

url="http://url:port/WSSec2LTPA"

headers = {'content-type': 'text/xml'}

body = """<soapenv:Envelope 
....... goes here ....
</soapenv:Envelope>
"""



response = requests.post(url,data=body,headers=headers)
soup = BeautifulSoup(response.content,"html5lib")
token = soup.find("wsse:binarysecuritytoken").text
