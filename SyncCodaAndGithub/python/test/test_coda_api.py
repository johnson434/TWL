import sys
import unittest

# import main.api.coda_api
# import main.data.coda_data
from main.api import coda_api
from main.data import coda_data


class TestCodaAPIEndToEnd(unittest.TestCase):
    def setUp(self):
        self.coda_api_key = coda_api_key = open("../../../token.txt", mode='r').readline()
        self.doc_id = "OBsatQ1Yn9"

    def test_list_pages(self):
        # 토큰 및 쿼리 파람 설정
        coda_api_key = self.coda_api_key
        doc_id = self.doc_id
        response = coda_api.listPages(coda_api_key=coda_api_key, doc_id=doc_id)
        assert type(response) is coda_data.ListPagesResponse

    def test_list_pages_with_wrong_app_key(self):
        response = coda_api.listPages(coda_api_key="wrong_app_key", doc_id='OBsatQ1Yn9')
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()