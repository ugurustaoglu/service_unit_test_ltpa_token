
from http_ltpa_get_uat import token

url_CustomerQueryService="url goes here"

body_CustomerQueryService = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Header>
      <wsse:Security soapenv:mustUnderstand="0" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
         <wsse:BinarySecurityToken ValueType="wsst:LTPA"
         xmlns:wsst="http://www.ibm.com/websphere/appserver/tokentype/5.0.2">""" +token.strip()+"""</wsse:BinarySecurityToken>
      </wsse:Security>
  
  .... soap req body goes here..........
      
</soapenv:Header>      
</soapenv:Envelope>"""