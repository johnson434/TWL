from api import coda_api
from log.custom_log import *
import sys
import time
import queue
import logging

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

def get_all_pages(visited_doc_set: set, id_name_dict: dict, coda_api_key, doc_id: str) -> dict:
    logger.debug('called')
    visited_doc_set.add(doc_id)
    listPagesResponse = coda_api.listPages(coda_api_key=coda_api_key, doc_id=doc_id)
    time.sleep(5)
    
    for item in listPagesResponse.items:
        if item.type == 'doc' and item.id not in visited_doc_set:
            visited_doc_set.add(item.id)
            get_all_pages(visitedDocSet=visited_doc_set, id_name_dict=id_name_dict, coda_api_key=coda_api_key, doc_id=item.id)
        elif item.type == 'page':
            id_name_dict[item.id] = item.name
    
    return id_name_dict
    

# todo : 제거해야됨
def main(): 
    logger.debug("start")
    coda_api_key = ""
    doc_id = "OBsatQ1Yn9"
    # 토큰 및 쿼리 파람 설정
    if len(sys.argv) < 2:
        coda_api_key = open("../../../token.txt", mode='r').readline()
    else:
        coda_api_key = sys.argv[1]

    # 모든 page id 조회
    idNameDict = get_all_pages(visited_doc_set=set(), id_name_dict=dict(), coda_api_key=coda_api_key,doc_id=doc_id)
    logger.info(f'avaliable pageList : {idNameDict}')
    
    request_page_list = queue.Queue()
    request_id_page_name_dict = dict()
    logger.info(f'idNameDict : {idNameDict}')
    # 페이지 출력
    for page_id, page_name in idNameDict.items():
        exportPageResponse = coda_api.export_page(coda_api_key=coda_api_key, doc_id=doc_id, page_id=page_id)
        time.sleep(3)
        if exportPageResponse is None:
            continue
        
        request_id_page_name_dict[exportPageResponse.request_id] = page_name
        request_page_list.put(exportPageResponse.request_id)
    
    # # check Status
    while not request_page_list.empty():
        request_id = request_page_list.get()
        page_name = request_id_page_name_dict[request_id]
        contextExportResponse = coda_api.requestContentExportStatus(coda_api_key=coda_api_key, doc_id=doc_id, page_id=page_id, request_id=request_id)

        if  contextExportResponse == None:
            request_page_list.put(id)
            time.sleep(3)
            continue
        
        coda_api.downloadLink(link=contextExportResponse.downloadLink, file_name=page_name, file_format=coda_api.FileFormat.Markdown)

main()