from api import coda_api
from log.custom_log import *
import sys
import time
import queue
import logging

# todo : 제거해야됨
# coda_api_key = open("../../token.txt", mode='r').readline()
doc_id = "OBsatQ1Yn9"

# # 로그 세팅
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 로깅 형식 설정
formatter = MethodNameFormatter('%(asctime)s - %(levelname)s - %(method_name)s - %(message)s')
console_handler.setFormatter(formatter)

# 로깅 핸들러 추가
logger.addHandler(console_handler)

# 테스트 로그
logger.debug("logger debug")

def main(): 
    logger.debug("start")
    # 토큰 및 쿼리 파람 설정
    args = sys.argv
    coda_api_key = args[1]

    # 가능한 페이지 출력
    list_pages = coda_api.listPages(coda_api_key=coda_api_key, doc_id=doc_id)

    # export page
    page_id = 'canvas-xbssZmCV_3'
    exportPageResponse = coda_api.export_page(coda_api_key=coda_api_key, doc_id=doc_id, page_id=page_id)
    request_id_list = queue.Queue()
    request_id_list.put(exportPageResponse)
    time.sleep(5)

    # check Status
    while not request_id_list.empty():
        tempResponse = request_id_list.get()

        link = coda_api.get_downloadLink(coda_api_key=coda_api_key, doc_id=doc_id, page_id=page_id, request_id=tempResponse.request_id)
        if  link == None:
            request_id_list.put(id)
            time.sleep(3)
            continue
        coda_api.downloadLink(link, 'sample_file', coda_api.FileFormat.Markdown)

main()