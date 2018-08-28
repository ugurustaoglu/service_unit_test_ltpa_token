#coding:utf8
import unittest
import requests
from customerqueryservice import url_CustomerQueryService
from customerqueryservice import body_CustomerQueryService
from bs4 import BeautifulSoup



class CustMgmtTest(unittest.TestCase):

    def test_CustomerQueryService(self):
        response = requests.post(url_CustomerQueryService, data=body_CustomerQueryService.encode('utf-8'))
        soup = BeautifulSoup(response.content, "html5lib")
        print(soup.prettify())
        taxofficename = soup.find("taxofficename").text
        self.assertEqual(taxofficename, 'String to Compare')

if __name__ == "__main__":
    unittest.main()


