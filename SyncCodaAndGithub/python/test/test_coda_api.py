import sys
import unittest

# import main.api.coda_api
# import main.data.coda_data
from main.api import coda_api
from main.data import coda_data


class TestCodaAPIEndToEnd(unittest.TestCase):
    def setUp(self):
        self.api_key = sys.argv[1]
        self.doc_id = "OBsatQ1Yn9"

    def test_list_pages(self):
        # 토큰 및 쿼리 파람 설정
        coda_api_key = self.api_key
        doc_id = self.doc_id
        response = coda_api.listPages(coda_api_key=coda_api_key, doc_id=doc_id)
        assert type(response) is coda_data.ListPagesResponse

    def test_list_pages_with_wrong_app_key(self):
        response = coda_api.listPages(coda_api_key="wrong_app_key", doc_id='OBsatQ1Yn9')
        self.assertIsNone(response)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise TypeError("주어진 매개 변수의 개수가 1개 이하입니다. 파일과 API 키를 넘겨주세요.")
    unittest.main(argv=sys.argv[:1])  # Pass only the script name to unittest.main()