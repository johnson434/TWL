from api import coda_api
import sys
import time
import queue

# todo : 제거해야됨
# coda_api_key = open("../../token.txt", mode='r').readline()
doc_id = "OBsatQ1Yn9"

def main():
    # 토큰 및 쿼리 파람 설정
    args = sys.argv
    coda_api_key = args[1]
    
    # 가능한 페이지 출력
    print("=====================listPages=====================")
    list_pages = coda_api.listPages(coda_api_key=coda_api_key, doc_id=doc_id)
    print(f'listPages : {list_pages}')

    # export page
    print("=====================export_page=====================")
    page_id = 'canvas-xbssZmCV_3'
    exportPageResponse = coda_api.export_page(coda_api_key=coda_api_key, doc_id=doc_id, page_id=page_id)
    print(f'exportPageResponse : {exportPageResponse}')
    request_id_list = queue.Queue()
    request_id_list.put(exportPageResponse)
    time.sleep(5)

    # check Status
    print("=====================check_status=====================")
    print(f'request_id_list : {request_id_list} request_id_list.empty {request_id_list.empty()} request_id_list.qsize : {request_id_list.qsize()}')
    while not request_id_list.empty():
        tempResponse = request_id_list.get()
        print(f'tempResponse : {tempResponse}')

        link = coda_api.get_downloadLink(coda_api_key=coda_api_key, doc_id=doc_id, page_id=page_id, request_id=tempResponse.request_id)
        if  link == None:
            print(f'request is in progrss. request_id : {id}')
            request_id_list.put(id)
            time.sleep(3)
            continue
        coda_api.downloadLink(link, 'sample_file', coda_api.FileFormat.Markdown)



main()